#!/bin/bash
echo -n 002299 Current Price:\ 
curl -s 'http://download.finance.yahoo.com/d/quotes.csv?s=002299.sz&f=l1' --connect-timeout 3
