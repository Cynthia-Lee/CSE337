#!/usr/bin/perl
#Cynthia Lee
#111737790
#cyllee
use strict;
use warnings;

#command line input
my $file = $ARGV[0];
open FILE, "<", $file or die "Can't open input file: $!";
my @e_file;
my @r_file;
my @w_file;
my @x_file;
my @t_file;
open E_OUTPUT, ">efiles.txt" or die "Can't open efiles.txt file: $!";
open R_OUTPUT, ">rfiles.txt" or die "Can't open rfiles.txt file: $!";
open W_OUTPUT, ">wfiles.txt" or die "Can't open wfiles.txt file: $!";
open X_OUTPUT, ">xfiles.txt" or die "Can't open xfiles.txt file: $!";
open T_OUTPUT, ">tfiles.txt" or die "Can't open tfiles.txt file: $!";
while (my $line =<FILE>) {
chomp $line;
if (-e $line) { #file exists
print E_OUTPUT "$line\n";
push @e_file, $line;
}
if (-r $line) { #file readable
print R_OUTPUT "$line\n";
push @r_file, $line;
}
if (-w $line) { #file writable
print W_OUTPUT "$line\n";
push @w_file, $line;
}
if (-x $line) { #file executable
print X_OUTPUT "$line\n";
push @x_file, $line;
}
if (-T $line) { #file text
print T_OUTPUT "$line\n";
push @t_file, $line;
}
}
close FILE;
close E_OUTPUT;
close R_OUTPUT;
close W_OUTPUT;
close X_OUTPUT;
close T_OUTPUT;
my $len = scalar @e_file;
print "$len existing files: @e_file\n";
$len = scalar @r_file;
print "$len readable files: @r_file\n";
$len = scalar @w_file;
print "$len writable files: @w_file\n";
$len = scalar @x_file;
print "$len executable files: @x_file\n";
$len = scalar @t_file;
print "$len plain text files: @t_file\n";