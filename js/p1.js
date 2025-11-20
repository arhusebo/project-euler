function* range(start = 0, end = Infinity, step = 1) {
	let iterationCount = 0;
	for (let i = start; i < end; i += step) {
		iterationCount++;
		yield i;
	}
	return iterationCount;
}


Set.prototype.sum = function() {
	return Array.from(this).reduce((x, y) => x+y, 0);
};


let a = [3, 5]
	.map((n) => new Set(range(0, 1000, n)))
	.reduce((x,y) => x.union(y), new Set())
	.sum()


console.log(a);
