const f = (c, p, s) => {
	n = c+p;
	sn = s+(!(n%2)?n:0);
	return n<4e6?f(n, c, sn):sn;
}

console.log(f(1, 0, 0));
