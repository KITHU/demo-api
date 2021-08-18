#!/bin/bash 

set -ex
set -o pipefail

echo "Clean the images and remove db from root dir"


cleanup() {
  echo "clean up begins"
  echo " "
  sudo rm -rf postgres_db
  echo "Database dir removal completed"

  echo "Stop all running containers"
  docker stop $(docker ps -a -q)
  
  echo "remove all stopped containers"
  docker rm $(docker ps -a -q)

  echo "begin Images removal"
  docker rmi -f $(docker images -a | awk {'print $3'})
}

main() {
  cleanup
}

main