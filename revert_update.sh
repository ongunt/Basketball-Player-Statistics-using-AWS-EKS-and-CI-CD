#!/usr/bin/env bash

kubectl rollout undo deployment/app --namespace=app

