#!/usr/bin/env perl


use FileHandle; #Import the file handling module ~~

open (my $fd, ">", "/dev/cpu_dma_latency") # Open up the file for writing '>'
    or die "Cannot open /dev/cpu_dma_latency for writing. Are you root?";

print $fd "0"; # Write to the file itself as needed

print "Press CTRL-C to end.\n"; 

while (1) { #Sleep, ie , do not close the program off
    sleep 5;
}

close $fd #Never going to get here, but for practice sake
    or warn "I could not close the File Handle that was used.";
