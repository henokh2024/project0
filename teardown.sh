#!/bin/bash

RESOURCE_GROUP="rg-project0-sre"

echo "Starting Azure resource cleanup ..."

az group delete \
   --name "$RESOURCE_GROUP" \
   --yes \
   --no-wait

   echo "Resource group deletion initiated."