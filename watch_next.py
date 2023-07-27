### Importing required modules
import spacy
nlp = spacy.load('en_core_web_md')

### Defining main function
def movie_selector(input_description):

    fo = open("movies.txt",'r')
    movie_dict = {}
    for line in fo:
        in_line = line.split(":")
        movie_dict[in_line[0]] = [nlp(in_line[1]),0]                # Allowing space for simularity score

    title_list = list(movie_dict.keys())

    compare_nlp = nlp(input_description)
    for title in title_list:
        movie_dict[title][1] = compare_nlp.similarity(movie_dict[title][0])

    best_match = title_list[0]

    for title in title_list:
        if movie_dict[title][1] > movie_dict[best_match][1]:        # Iterating through to find best match
            best_match = title

    return best_match

compare_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print(movie_selector(compare_description))







                 


