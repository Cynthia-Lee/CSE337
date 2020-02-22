#!/usr/bin/perl
#Cynthia Lee
#111737790
#cyllee
use strict;
use warnings;

my $path = `echo \$PATH`;
my @directories = $path =~ /[\w.-]+/g;
print join("\n",@directories), "\n";