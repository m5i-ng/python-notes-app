#!/bin/bash
URL=http://localhost:8080/notes
METHOD=("GET" "POST" "DELETE" "PUT")

for i in {1..600}
do
      m=${METHOD[RANDOM%4]}
      randstring=`cat /dev/random | tr -d -c 0-9a-zA-Z | head -c 16`
      if [[ $m == "GET" ]]; then
          curl --silent -o /dev/null -X $m "${URL}"
      elif [[ $m == "POST" ]]; then
         curl --silent -o /dev/null -X $m "${URL}?desc=$randstring"
      else     
         curl --silent -o /dev/null -X $m "${URL}?id=$i&desc=$randstring"
         fi
      sleep 3
      echo ""
done 
