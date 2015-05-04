import json

def match_pairs(primary, secondary, pairs={}):
    match_counter = 0
    for primary_name in primary:
        primary_person = primary[primary_name]
        if (primary_person['partner']):
            continue
        for secondary_name in primary_person['rankings']:
            secondary_person = secondary[secondary_name]
            result = propose(primary_person, secondary_person)
            if (result):
                match_counter += 1
                if (secondary_person['partner']):
                    previous_partner = primary[secondary_person['partner']]
                    previous_partner['partner'] = None
                    del pairs[previous_partner['name']]
                primary_person['partner'] = secondary_person['name']
                secondary_person['partner'] = primary_person['name']
                pairs[primary_person['name']] = primary_person['partner']
                break
    if (match_counter > 0):
        return match_pairs(primary, secondary, pairs)
    else:
        return pairs

def propose(primary_person, secondary_person):
    if (secondary_person['partner']):
        return (secondary_person['rankings'].index(primary_person['name']) < secondary_person['rankings'].index(secondary_person['partner']))
    else:
        return True

def format_data(data):
    formated_data = {}
    for key in data:
        formated_data[key] = {
            "name": key,
            "rankings": data[key],
            "partner": None
        }
    return formated_data

if (__name__=='__main__'):
    pass
