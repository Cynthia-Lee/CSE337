#!/usr/bin/perl
#Cynthia Lee
#111737790
#cyllee
use strict;
use warnings;

#command line input
my $file = $ARGV[0];
open FILE, "<", $file or die "Can't open input file: $!";
while (my $line =<FILE>) {
my $result = $line;
if ($line =~ /<p>[\w\W]*<\/p>/g) {
$result = substr($line, 3, -5);
$result .= "<br><br>\n";
}
$result =~ s/<span>//g;
$result =~ s/<\/span>//g;
print "$result";
}
close FILE;