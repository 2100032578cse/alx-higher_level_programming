#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
	const outp = list.reduce(((count, temp){
		if (temp===searchElement){
			count = 1;
		}else{
			count = 0;
		}
	}),0);
	return outp;
};
