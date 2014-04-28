
/*
	Quicksort reference: http://www.nczonline.net/blog/2012/11/27/computer-science-in-javascript-quicksort/  
	Checking arr for at least one element of obj (if obj is an array) or obj if obj is not
	if obj is an array: 
		returns true if at least one value in arr is in Array
	else returns whether the value obj is contained in Array 
*/
function contains (arr,obj) {
	if (obj instanceof Array) {
		var contains = false;
		obj.forEach(function(elem) {
			if (arr.indexOf(elem) > -1) {
				contains = true;
				return false; //break
			}
		});
		return contains;
	}
	return arr.indexOf(obj) > -1;
}

var genres = ['Action & Adventure','Animation','Art House & International',
	'Classics','Comedy','Drama','Horror','Kids & Family','Mystery & Suspense','Romance',
	'Science Fiction & Fantasy','Documentary','Musical & Performing Arts','Special Interest',
	'Sports & Fitness','Television','Western'];

var Order = {
	'high' : 1,
	'low' : 0
};

// call this function to get the data.
// example call: get_data(used, unused, [2007,2008], ["Horror","Comedy"], ["PG-13","R"], "Worldwide", Order.high);
/*
	used: *return value* sorted list of data
	unused: *return value* list of movies (in alphabetical order by year) of movies that 
			meet the criteria, but do not provide sufficient data (ex: no 'foreign' data
			if we were sorting on which movie grossed the most in foreign countries)
	genres: selected genres ([] if none selected)
	years: selected years ([] if none selected)
	ratings: selected ratings ([] if none selected)
	studios: selected studios ([] is none selected)
	variable: name of variable we are comparing (ex. Worldwide, Number_of_Theatres_in_Opening_Weekend, etc.)
	order: Order.high or Order.low
*/
function get_data (years, genres, ratings, variable, order) {
	used = new Array();
	unused = new Array();
	var charMax = 0;
	movies.forEach(function(movie) {
		//new code to test maxes

		// figure out which movies to use
		if (contains(years,movie.Year) && contains(genres,movie.Genres) && 
			contains(ratings,movie.Rating)) {
			if (movie[variable] == null) 
				unused.push(movie);
			else {
				used.push(movie);
			}
		}
	});
	// sort the movies we are using based on variable
	used = quickSort(used, order, variable);
	return {"data": used, "unused": unused};
}



function swap(items, firstIndex, secondIndex){
    var temp = items[firstIndex];
    items[firstIndex] = items[secondIndex];
    items[secondIndex] = temp;
}

function partition(order, items, left, right, variable) {

    var pivot = items[left][variable],
    	i = left,
    	j = right;

    while (i <= j) {

        if (order == Order.low) {
	        while (items[i][variable] < pivot) {
	            i++;
	        }
	        while (items[j][variable] > pivot) {
	            j--;
	        }
	    } else if (order == Order.high) {
	    	while (items[i][variable] > pivot) {
	            i++;
	        }
	        while (items[j][variable] < pivot) {
	            j--;
	        }
	    }

        if (i <= j) {
            swap(items, i, j);
            i++;
            j--;
        }
    }

    return i;
}

function recursiveQuickSort(items, left, right, order, variable) {

    var index;

    if (items.length > 1) {

        index = partition(order, items, left, right, variable);

        if (left < index - 1) {
            recursiveQuickSort(items, left, index - 1, order, variable);
        }

        if (right > index) {
            recursiveQuickSort(items, index, right, order, variable);
        }

    }

    return items;
}

function quickSort(arr, order, variable) {
	return recursiveQuickSort(arr, 0, arr.length - 1, order, variable);
}
