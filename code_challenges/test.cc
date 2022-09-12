

int x ;

int * const ptr = &x;
int y;

void func1(void) {
ptr = &y;
}
