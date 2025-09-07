#!/bin/bash
# TechSphere Corporation - Log Cleanup Utility
# WARNING: Irreversible deletion

TARGET_DIR=/var/logs/archive
echo "Cleaning logs from $TARGET_DIR"
rm -rf $TARGET_DIR/*
echo "Cleanup finished at $(date)"
