#include <stdio.h>
#include <string.h>

#include <ncurses.h>

int process_args(int argc, char *argv[], int *tail) {
    *tail = argc==2 && strcmp(argv[1], "tail") == 0;
    if (argc==2 && strcmp(argv[1], "-h") == 0) {
        printf("Usage: cursor [-h|tail]\n");
        printf("\ttail\tleave a tail\n");
        printf("\t-h\tthis message\n");
        return 1;
    }
    return 0;
}

void initialize() {
    initscr(); // initialize ncurses
    clear(); // clear the screen
    curs_set(0); // turn off cursor
    cbreak(); // do not buffer input
    noecho(); // do not echo input
}

void teardown() {
    endwin();
}

void header() {
    printw("Use keypad to move cursor (8, 4, 2, 6).\n0 exits.\nAny other key will change cursor.\n");
}

void process(int tail) {
    int c;
    int row = 5;
    int col = 5;
    int prev_c;
    prev_c = mvwinch(stdscr, row, col);
    char point = ’+’;
        mvaddch(row, col, point);
    while((c = getch())!= ’0’) {
        if (!tail) {
            mvaddch(row, col, prev_c);
        }
        switch(c) {
            case ’8’: row -= 1; break;
            case ’2’: row += 1; break;
            case ’4’: col -= 1; break;
            case ’6’: col += 1; break;
            default: point = c;
        };
        prev_c = mvwinch(stdscr, row, col);
        mvaddch(row, col, point);
    }
}
int main(int argc, char *argv[]) {
    int tail = 0;
    int rv = process_args(argc, argv, &tail);
    if (rv)
        return rv;
    initialize();
    header();
    process(tail);
    return 0;
}
