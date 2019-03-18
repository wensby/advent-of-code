BIN_DIR=./bin
SRC_DIR=./src
TEST_DIR=./test
SHELL := /bin/bash
CC = gcc
SOURCES := $(wildcard $(SRC_DIR)/*.c)
solutions := $(addsuffix .solution, $(basename $(SOURCES)))
all-tests := $(addsuffix .test, $(basename $(wildcard $(TEST_DIR)/*.input)))
TEST_COUNT = 0

.PHONY : build test all %.test

build: $(solutions)
	@echo "Build complete!"

%.solution: %.c
	$(eval output=$(patsubst %.c, %, $(notdir $<)))
	@echo "Compiling $(output)"
	@$(CC) $< -o $(BIN_DIR)/$(output)

%.test: %.input %.output
	$(eval object=$(shell echo | awk '{match("'"$<"'", /[0-9]{4}-[0-9]{2}-[0-9]/); print substr("'"$<"'", RSTART, RLENGTH);}'))
	@echo "$<"
	@$(BIN_DIR)/$(object) < $< 2>&1 | diff $(word 2, $?) - || true;
	$(eval TEST_COUNT=$(shell echo $$(($(TEST_COUNT)+1))))

test: $(all-tests)
	@echo '$(TEST_COUNT) tests run!'

clean:
	@rm -if $(BIN_DIR)/*
	@echo "Cleanup complete!"

all: clean build test	
