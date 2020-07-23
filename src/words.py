import random

#random list of words that returns a randmoized word when called  - girls names
def secret_word_girls_names():
    word_list = {"girls_names": ["charlotte","olivia","ava","amelia","mia","isla","grace","ella","chloe","harper","zoe","sophie","evie","evelyn","isabella","ruby","ivy"
                                 "matilda","lucy","sophia","aria","georgia","sienna","scarlett","hannah","emma","zara","abigail","isabelle","audrey","layla","mila","lily",
                                 "violet","alice","hazel","piper","ellie","mackenzie","poppy","annabelle","sofia","maya","savannah","penelope","frankie","eva","willow",
                                 "maddison","ivy","jasmine","violet","elizabeth","stella","phoebe","aurora","imogen","billie","alexis","summer","addison",
                                 "harriet","ayla","eleanor","eloise","madison","freya","elsie","claire","rose","emilia","florence","daisy","lily","sarah","eden","anna",
                                 "eliza","holly","lola","bella","ariana","lara","luna","indiana","harlow","madeleine","chelsea","bonnie","quinn","aaliyah",
                                 "heidi","victoria","isabel","elena","peyton","millie","Madeline","charlie","jessica","olive",]
                 }

    secret_word = random.choice(word_list.get("girls_names"))
    return secret_word

#random list of words that returns a randmoized word when called - generic list
def secret_word_generic():
    word_list = {"misc": ["abusive","wheel","watery","highfalutin","carry","vein","exuberant","nebulous","listen","horrible","position","enter","suspect","plants",
                          "clever","draconian","damage","rightful","squeeze","kiss","communicate","aboriginal","birds","bored","statuesque","new","star","sordid",
                          "steady","simple","drag","boring","hissing","perpetual","aback","beneficial","prepare","false","edge","wrathful","announce","tangible",
                          "cause","homeless","pretend","orange","zoo","various","brake","gleaming","boat","abrasive","symptomatic","airplane","silky","sleet","understood",
                          "white","tightfisted","greet","scattered","doll","stone","suggestion","rough","endurable","horn","cry","injure","duck","mice","truck","brother",
                          "mend","trousers","pet","start","mixed","boundary","reproduce","canvas","travel","awesome","girls","sticks","rings","adorable","graceful",
                          "look","stage","desert","large","cows","sock","government","heartbreaking","collar",]}
    secret_word = random.choice(word_list.get("misc"))
    return secret_word


def secret_string_word(secret_word):                            #Generates the secrete game board
    hidden_word_list = []
    count = 0
    length_of_secret_word = len(secret_word)
    while count < length_of_secret_word == len(secret_word):
        hidden_word_list.insert(0, "  _  ")
        count += 1
    return hidden_word_list


                                                                #money money money moneeeeeeeeeeey - randomised for the "spin" effect
def cash_value():
    cash_values = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,
                   1900,
                   2000, "bankruptcy", "bankruptcy"]
    value = random.choice(cash_values)
    if value == "bankruptcy":
        return 0
    else:
        return value
