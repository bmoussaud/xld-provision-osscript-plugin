#!/bin/sh
set -x
echo "Executing script ${scripted.file.path} "
chmod +x ${scripted.file.path}
./${scripted.file.path}

