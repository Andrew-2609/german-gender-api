[![Deploy to Deta](https://github.com/Andrew-2609/german-gender-api/actions/workflows/deta-deploy.yml/badge.svg?branch=main)](https://github.com/Andrew-2609/german-gender-api/actions/workflows/deta-deploy.yml)

# German Gender API

Have you ever had to search the internet for the grammatical gender of a German word, and felt it could be easier?

That was very specific, I know. And the chances of you being a developer and a German student at the same time aren't
that great (about one in 901.4 thousand if you're German - according
to [statista.com](https://www.statista.com/statistics/957876/professional-developers-in-europe/#:~:text=This%20statistic%20shows%20the%20number,over%20901%2C4%20thousand%20developers.))
.

Well, if that's the case, this API is **made for you**. It will give you the **grammatical gender** of the noun you
want, as well as the **articles** related to that gender (nominative, accusative, dative and genitive, if they are
useful for you).

## The Database

Currently, there are over **100,000 nouns** in the database used by this API. Unfortunately, it is a bit hard to
make your own database of German nouns without making tons of requests in German dictionary websites.

I did my best to gather as many as I could, not to mention the several checks for misspelling and gender issues.

I will be constantly updating the data, so if you know that a certain noun should be in the database, but it is not,
please **let me know**!

## The Genders

**Masculine**, **feminine**, or **neuter**?

There are some **rules** for figuring out the grammatical gender of a noun in German, but in general you have to figure
it out by yourself.

I've applied the most general rules in a loop to save the nouns in the database with their supposed genders, but even
for the few rules that exist, **there are exceptions**.

The words that don't fit any of the rules I used (over **75,000**) were saved as "**tdb**" (to be defined), which means they
will be corrected in the future.

So if you come across a word with the wrong gender or the gender *to be defined*, please **let me know**! 