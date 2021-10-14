import sys
import getopt
import random

sv_good_words = ['sopprot', 'pulver', 'knickedick', 'planta',
                 'praktarsle', 'plattfot', 'potatisgris', 'rötägg', 'skabbhals',
                 'slappsvans', 'dummerjöns', 'fåntratt', 'blindstyre',
                 'hönshjärna', 'talglymmel', 'storsnorkare', 'snortut', 'snorslev',
                 'skinnbracka', 'kräkla', 'skabbråtta', 'skojare', 'gnällspik',
                 'gnet', 'snorvalp', 'tjockskalle', 'tångräka', 'gallfåne',
                 'ärkebandit', 'enfälling', 'svinpäls', 'syltrygg', 'pottsork',
                 'morsgris', 'drummel', 'lortpåse', 'bondlurk', 'dyngspridare',
                 'gamla-knölsvan', 'kanalje', 'krämare', 'hagga', 'luskung',
                 'pajas']

en_good_words = ['ass', 'hole', 'amcik', 'andskota', 'anus', 'arschloch',
                 'arse', 'ash0le', 'asholes', 'ass', 'assface',
                 'assh0le', 'assh0lez', 'asshole', 'assholz',
                 'assmonkey', 'assrammer', 'asswipe', 'ayir', 'azzhole',
                 'b00bs', 'b17ch', 'b1tch', 'bassterds', 'bastard',
                 'bastardz', 'basterds', 'basterdz', 'bch', 'bi7ch',
                 'biatch', 'bich', 'bitch', 'blowjob', 'boffing',
                 'boiolas', 'bollock', 'boobs', 'breasts', 'btch',
                 'buceta', 'bullshit', 'butthole', 'buttpirate',
                 'buttwipe', 'c0ck', 'c0k', 'cabron', 'carpetmuncher',
                 'cawk', 'cazzo', 'chink', 'chraa', 'chuj', 'cipa',
                 'clit', 'cnts', 'cntz', 'cock', 'cockhead',
                 'cocksucker', 'crap', 'cum', 'cunt', 'cuntz', 'd4mn',
                 'damn', 'daygo', 'dego', 'dick', 'dike', 'dild0',
                 'dild0s', 'dildo', 'dilld0', 'dilld0s', 'dirsa',
                 'dominatricks', 'dominatrics', 'dominatrix', 'dupa',
                 'dyke', 'dziwka', 'ejackulate', 'ejakulate', 'ekrem',
                 'ekto', 'enculer', 'enema', 'faen', 'fag', 'fag1t',
                 'faget', 'fagg1t', 'faggit', 'faggot', 'fagit', 'fagz',
                 'faig', 'fanculo', 'fanny', 'fart', 'fatass', 'fcuk',
                 'feces', 'feg', 'felcher', 'ficken', 'fitt', 'flikker',
                 'flipping', 'foreskin', 'fotze', 'fuchah', 'fuck',
                 'fucka', 'fucker', 'fuckin', 'fucking', 'fudgepacker',
                 'fukah', 'fuken', 'fuker', 'fukin', 'fukka', 'fukkah',
                 'fukken', 'fukker', 'fukkin', 'futkretzn', 'fux0r',
                 'g00k', 'gay', 'gaybor', 'gayboy', 'gaygirl', 'gayz',
                 'goddamned', 'gook', 'guiena', 'h00r', 'h0ar', 'h0r',
                 'h0re', 'h4x0r', 'hell', 'helvete', 'hoar', 'hoer',
                 'honkey', 'hoor', 'hoore', 'hore', 'huevon', 'hui',
                 'injun', 'jackoff', 'jap', 'jerkoff', 'jisim', 'jism',
                 'jiss', 'jizm', 'jizz', 'kanker', 'kawk', 'kike',
                 'klootzak', 'knob', 'knobz', 'knulle', 'kraut',
                 'kuksuger', 'kunt', 'kuntz', 'kurac', 'kurwa', 'kusi',
                 'kyrpa', 'l3i+ch', 'l3itch', 'lesbian', 'lesbo',
                 'lezzian', 'lipshits', 'lipshitz', 'mamhoon',
                 'masochist', 'masokist', 'massterbait', 'masstrbait',
                 'masstrbate', 'masterbaiter', 'masterbat',
                 'masterbat3', 'masterbate', 'masturbat', 'masturbate',
                 'merd', 'mibun', 'mofo', 'monkleigh', 'motha',
                 'mothafucker', 'mothafuker', 'mothafukkah',
                 'mothafukker', 'motherfucker', 'motherfukah',
                 'motherfuker', 'motherfukkah', 'motherfukker',
                 'mouliewop', 'muie', 'mulkku', 'muschi', 'mutha',
                 'muthafucker', 'muthafukah', 'muthafuker',
                 'muthafukkah', 'muthafukker', 'n1gr', 'nastt', 'nasty',
                 'nazi', 'nepesaurio', 'nigga', 'niggas', 'nigger',
                 'nigur', 'niiger', 'niigr', 'nutsack', 'orafis',
                 'orgasim', 'orgasm', 'orgasum', 'oriface', 'orifice',
                 'orifiss', 'orospu', 'p0rn', 'packi', 'packie',
                 'packy', 'paki', 'pakie', 'paky', 'paska', 'pecker',
                 'peeenus', 'peeenusss', 'peenus', 'peinus', 'pen1s',
                 'penas', 'penis', 'penisbreath', 'penus', 'penuus',
                 'perse', 'phuc', 'phuck', 'phuk', 'phuker', 'phukker',
                 'picka', 'pierdol', 'pillu', 'pimmel', 'pimpis',
                 'piss', 'pizda', 'polac', 'polack', 'polak', 'poonani',
                 'poontsee', 'poop', 'porn', 'pr0n', 'pr1c', 'pr1ck',
                 'pr1k', 'preteen', 'pula', 'pule', 'pusse', 'pussee',
                 'pussy', 'puta', 'puto', 'puuke', 'puuker', 'qahbeh',
                 'queef', 'queer', 'queerz', 'qweers', 'qweerz',
                 'qweir', 'rautenberg', 'recktum', 'rectum', 'retard',
                 's.o.b.', 'sadist', 'scank', 'schaffer', 'scheiss',
                 'schlampe', 'schlong', 'schmuck', 'screw', 'scrotum',
                 'semen', 'sex', 'sexx', 'sexxx', 'sexy', 'sh1ter',
                 'sh1ts', 'sh1tter', 'sh1tz', 'sharmuta', 'sharmute',
                 'shemale', 'shi+', 'shipal', 'shit', 'shitt',
                 'shitter', 'shitty', 'shity', 'shitz', 'shiz', 'shyte',
                 'shytty', 'skanck', 'skank', 'skankee', 'skankey',
                 'skanky', 'skrib', 'slut', 'slutty', 'slutz', 'smut',
                 'sonofabitch', 'sx', 'teets', 'teez', 'testical',
                 'testicle', 'tit', 'titt', 'turd', 'va1jina', 'vag1na',
                 'vagiina', 'vagina', 'vaj1na', 'vajina', 'vullva',
                 'vulva', 'w00se', 'w0p', 'wank', 'wh00r', 'wh0re',
                 'whoar', 'whore', 'xrated', 'xxx']


def usage():
    print(f'Usage: {name} -n <number of words> -l <language, en or sv>')
    sys.exit(2)


if __name__ == '__main__':
    name = sys.argv[0]
    length = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:l:")
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-n':
            try:
                length = int(arg)
            except Exception:
                usage()
        elif opt == '-l':
            if arg == 'en':
                good_words = en_good_words
            elif arg == 'sv':
                good_words = sv_good_words
            else:
                usage()
        else:
            print("I don't understand that argument.")
            sys.exit(2)

    password = []
    for _ in range(length):
        password.append(random.choice(good_words))

    print('-'.join(password))
