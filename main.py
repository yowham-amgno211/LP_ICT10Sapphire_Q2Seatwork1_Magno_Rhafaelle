from pyscript import document

def candidate_checker(e):
    club_members = ['becca vinco', 'athena silva', 'luis solis', 'mikey robles', 'rj magno', 'divine lipura', 'pio serdena', 'max calata', 'jacob opilla', 'nathan bernaldez']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name +  ' '  + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations, {candidate}! You are now part of the Glee Club.') 

    document.getElementById('result').innerHTML =messages[member_checker]