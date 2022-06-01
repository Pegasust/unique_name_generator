#!/usr/bin/env bash
for jsonnet_file in $(ls data/jsonnet/*.jsonnet); do
    echo "jsonnet $jsonnet_file &"
    jsonnet $jsonnet_file &
done
wait # wait for all children processes
# move all of the json inside data/jsonnet to data/
mv data/jsonnet/*.json data/