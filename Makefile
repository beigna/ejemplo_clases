SHELL := /bin/bash
container_name := benedetti_kiu

DOCKER_RUN_BASE := docker run -it --rm
DOCKER_RUN_BASE += --volume $(shell pwd):/opt/app
DOCKER_RUN_BASE += --user $(shell id -u):$(shell id -g)
DOCKER_RUN_BASE += --net=host $(container_name)-dev:latest

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

docker-build-dev: ## Build the Docker development image
	docker build -t $(container_name)-dev -f Dockerfile.dev .

docker-pytest-watch: ## Run test on change
	$(DOCKER_RUN_BASE) pytest-watch

docker-test: ## Run test on change
	$(DOCKER_RUN_BASE) pytest
