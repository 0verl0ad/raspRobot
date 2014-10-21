"""Usage: myWeatherLocation.py --city=city

Options:
    --city=city Name of the city
"""

import pywapi
import docopt

def main():
    try:
        arguments = docopt.docopt(__doc__)
        city = arguments['--city']
    except docopt.DocoptExit as e:
        print(e)
    else:
        p = pywapi.get_location_ids(city.lower())
        for i, ci in enumerate(p):
            print(i, ' -> ' + p[ci] + ' -- ' + ci  )

if __name__ == '__main__':
    main()
