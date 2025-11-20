function* range(start = 0, end = Infinity, step = 1) {
	let iterationCount = 0;
	for (let i = start; i < end; i += step) {
		iterationCount++;
		yield i;
	}
	return iterationCount;
}


function pfac(n, sup=1) {
	if (n==1) return sup;
	let d=Array.from([...range(2, n**0.5), 1]).find((d)=>n%d==0)
	return d==1&&n>sup?n:pfac(n/d, sup);
}

console.log(pfac(600851475143));
