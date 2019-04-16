var request = require('request'),
    cheerio = require('cheerio');

if(false)
	request('https://news.ycombinator.com', function(err, response, html) {
        if (err)
            throw (err)
        console.log(html);
    })

// Attain all of the information from the yCombinator home site
if (false)
    request('https://news.ycombinator.com', function(err, response, html) {
        if (err)
            throw (err)

        // Load the content of the HTML into the Cheerio Format (Object?)
        let $ = cheerio.load(html);
        /* 
        someArticle(siteName)

        Grabs all span type blocks with id comhead
        For this particular scenario, each of the refered to links would be
        the siteName from aboves format.   
        */
        $('span.comhead').each(function(i, elt) {
            // Show all of the siteName sections
            console.log($(this).text())
                /*		
        Goes to the previous section from the currently pointed to (Anchor?)
    	In this case it would be the title of the article being 
		pointed to, whose comName was the handle prior
		*/
            let a = $(this).prev();
            console.log(a.text())
        })
    })

if (true)
    request('https://news.ycombinator.com', function(err, response, html) {
        if (err)
            throw (err)

        let $ = cheerio.load(html);
        $('span.comhead').each(function(i, element){
        	let a = $(this).prev();

        	// Get the rank by parsing the element two levels above the "a" element:
        	let rank = a.parent().parent().text();
        	
        	let title = a.text();
        	
        	// Parse the href attribute from the "a" element
        	let url = a.attr('href');
        	
        	// Get the subtext children from the next row in the HTML table:
        	let subtext = a.parent().parent().next().children('.subtext').children();
        	
        	//Extract the relevant data from the children
        	let points = $(subtext).eq(0).text();
        	let username = $(subtext).eq(1).text();
 			let comments = $(subtext).eq(2).text();

 			let metadata = {
 				rank: parseInt(rank),
 				title,
 				url,
 				points:parseInt(points),
 				username,
 				comments:parseInt(comments)
 			};
	     console.log(metadata)
        })
   
    })
