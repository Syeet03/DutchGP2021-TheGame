print('''
--------------Dutch GP 2021 The Game--------------
--------------Maker: Lucas van Pelt---------------
__________________________________________________''')

coureurNaam = input('Met welke coureur wil je het spel spelen?: ')
coureurVS   = input('Welke coureur wil je als tegenstander hebben?: ')
coureurTeam = input('Wie wil je als teamgenoot?: ')

print('___________________________________________')
print('Speler: ' + str(coureurNaam))
print('Tegenstander: ' + str(coureurVS))
print('Teamgenoot: ' + str(coureurTeam))
print('___________________________________________')

print('Je start aan de linker kant van de baan, ' + str(coureurVS) + ' start rechts van je. \nJullie komen samen op de eerste bocht af denderen. \nGa jij de binnenkant verdedigen of speel je op safe zodat je de eerste bocht doorkomt')

print('___________________________________________')

keuze1A = input('Ga jij voor Safe of ge je voor Uitremmen? Safe/Uitremmen ')
if keuze1A == "Safe":
    print('Gefeliciteerd! '+ str(coureurNaam) + ' Je bent door de eerste bocht! Je gaat nu door naar de volgende bocht')

    keuze1B = input('Je rijdt naast ' + str(coureurVS) + ' naar bocht 2, ga je hem uitremmen? Ja/Nee ')
    if keuze1B == "Ja":
        print('Je blokkeert je banden en botst bijna tegen ' + str(coureurVS) + ' op. \nJe banden hebben flatspots, je kan niet meer verder op deze banden, je moet een pitstop maken voor nieuwe banden')

        print('Je bent in de pits aangekomen, ga jij voor de medium banden en daarmee nog 1 keer naar binnen te moeten of ga je voor de harde banden en zorg dat dit je laatste pitstop is. \n(Let op, het gaat erg krap worden met de leeftijd van de banden!)')
        keuze1C = input('Medium of Hard: ')
        if keuze1C == "Medium":
            print('Je rijdt de pit uit, je licht op de laatste plek')

            print('Je gaat erg hard, je gaat veel autos voorbij, je hebt zicht op de 10e plaats, dat is je teamgenoot!. \nJe teamgenoot krijgt teamorders dat hij jouw voorbij moet laten gaan omdat jij sneller bent. \nJe teamgenoot wilt en gaat niet aan de kant, jij beslist om een gewaagde inhaal actie te doen in bocht 11.')

            keuze1D = input('Ga je genoeg ruimte voor ' + str(coureurTeam) + ' overhouden over laat je hem geen ruimte over? Genoeg/Geen ')
            if keuze1D == "Genoeg":
                print('Je laat te veel ruimte over waardoor je in de grindbak komt, je kan gelukkig gelijk weer de baan op. ' + str(coureurTeam) + ' licht nog steeds voor je')

                print('Een paar ronden later rijdt je weer tegen de achterkant van ' + str(coureurTeam) + ', deze keer laat ' + str(coureurTeam) + ' je voorbij. \nJe licht op de 10e plek')

                print('Je gaat nog erg hard en je rijdt op de 5e plek maar je banden beginnen het te begeven. \nJe rijdt op ronde 50 en nog maar met 22 rondes te gaan. \nGa je op deze banden door of ga je naar de pitstop en switch naar nieuwe mediums, je raakt dan 2 plekken kwijt maar je gaat dan wel weer sneller als je tegenstanders. Pitstop/Doorrijden ')
                keuze1E = input('Pitstop of Doorrijden')
                if keuze1E == "Pitstop":
                    print('Je maakt een pitstop en het is een wereld pitstop! \n1.79 seconden, een nieuw wereldrecord! \nAls je de baan weer op komt rijden rijdt je op de 7e plek')

                    print('Met nog 21 rondes te gaan rijd de hele top 10 op de harde band op' + str(coureurVS) + ' en jij na.')

                    print('Op ronde 69 van de 72 rijd je 0.500 seconden achter'+ str(coureurVS) + '. ' + str(coureurVS) + ' rijd op dat moment eerste')

                    keuze1F = input('De laatste ronde gaat in, ga je ' + str(coureurVS) + ' proberen uit te remmen in de 1ste bocht? Ja/Nee ')
                    if keuze1F == "Ja":
                        print('Je hebt ' + str(coureurVS) + ' ingehaald! Dit is de laatste ronde!')

                        keuze1G = input('Ga je nog proberen om de snelste race ronden te rijden voor 1 punt, je banden zijn wel op! Ja/Nee ')
                        if keuze1G == "Ja":
                            print('De banden kunnen het niet meer, je rechterachterwiel begeeft het! Je eindigt in de grindbak en kan niet meer verder.')

                            print( str(coureurVS) + ''' heeft de race gewonnen en daardoor is hij eerste in het kampioenschap \n
                            Game Over!
                            ''')
                        else:
                            keuze1G == "Nee"
                            print('Je probeert ' + str(coureurVS) + ' achter je te houden, het is nog erg spannend maar jij hebt nieuwere banden als ' + str(coureurVS) + ' en je rijdt in de laatste sector van hem vandaan')

                            print('Gefeliciteerd, jij hebt de Dutch GP 2021 gewonnen!')

                    else:
                        keuze1F == "Nee"
                        print( str(coureurVS) + ' rijdt nog voor je, dit was de laatste kans om ' + str(coureurVS) + ' in te halen')

                        print( str(coureurVS) + ''' heeft de race gewonnen, jij bent 2e geworden, helaas! \n
                        Game Over!
                        ''')

                else:
                    keuze1E == "Doorrijden"
                    print('Je banden zijn op, je raakt weer posities kwijt')

                    keuze2E1 = input('Doordat je geen banden hebt gewisseld gaan je banden eraan, wil je je posities behouden of wil zachter gaan rijden en de zekerheid hebben dat je de finish lijn haalt? ')
                    if keuze2E1 == "Behouden":

                        print('''Doordat je posities wilt behouden zijn je banden eraan gegaan en daardoor heb je klapband gehad, je bent uit de race \n
                        Game Over!
                        ''')
                    else:
                        keuze2E1 == "Zekerheid"
                        print('Je hebt gekozen om zachter te gaan rijden zodat je de race wel finisht')

                        print('Dat was een goede keuze, je hebt de race gefinisht, niet op het podium. Maar je bent op de 13e plek geëindigd, niet optimaal maar je hebt de race gefinisht')


            else:
                keuze1D == "Geen"
                print('Je douwt ' + str(coureurTeam) + ' van de baan af, ' + str(coureurTeam) + ' botst tegen de muur aan en verliest zijn voor vleugen. \nJe krijgt aan het einde van de race 10 seconden straf!')

                print('''Je eindigt als 1ste maar daar komen nog 10 seconden tijdstraf bij, je bent 3e geworden \n
                Game Over!
                ''')

        else:
            keuze1C == "Hard"
            print('Je rijdt de pit uit, je licht op de laatste plek')

            print('Je gaat erg hard, je gaat veel autos voorbij, je hebt zicht op de 10e plaats maar je teamgenoot rijd op die plaats. \nJe teamgenoot krijgt teamorders dat hij jouw voorbij moet laten gaan omdat jij sneller bent. \nJe teamgenoot wilt en gaat niet aan de kant, jij beslist om een gewaagde inhaal actie te doen in bocht 11.')
            
            keuze2D = input('Ga je genoeg ruimte voor Perez overhouden over laat je hem geen ruimte over? Genoeg/Geen ')
            if keuze2D == "Genoeg":
                print('Je laat te veel ruimte over waardoor je in de grindbak komt, je kan gelukkig gelijk weer de baan op. ' + str(coureurTeam) + ' licht nog steeds voor je')

                print('Een paar ronden later rijdt je weer tegen de achterkant van '+ str(coureurTeam) + ', deze keer laat Perez je voorbij. \nJe licht op de 10e plek')

                print('Je gaat nog erg hard en je rijdt op de 5e plek maar je banden beginnen het te begeven. \nJe rijdt op ronde 50 en nog maar met 22 rondes te gaan. \nGa je op deze banden door of ga je naar de pitstop en switch naar nieuwe mediums, je raakt dan 2 plekken kwijt maar je gaat dan wel weer sneller als je tegenstanders.')
                keuze2E2 = input('Pitstop of Doorrijden')
                if keuze2E2 == "Pitstop":
                    print('Je maakt een pitstop en het is een wereld pitstop! \n1.79 seconden, een nieuw wereldrecord! \nAls je de baan weer op komt rijden rijdt je op de 7e plek')

                    print('Met nog 21 rondes te gaan rijd de hele top 10 op de harde band op ' + str(coureurVS) + ' en jij na.')

                    print('Op ronde 69 van de 72 rijd je 0.500 seconden achter ' + str(coureurVS) + '. ' + str(coureurVS) + ' rijd op dat moment eerste')

                    keuze2F = input('De laatste ronde gaat in, ga je' + str(coureurVS) + ' proberen uit te remmen in de 1ste bocht? Ja/Nee ')
                    if keuze2F == "Ja":
                        print('Je hebt ' + str(coureurVS) + ' ingehaald! Dit is de laatste ronde!')

                        keuze2G = input('Ga je nog proberen om de snelste race ronden te rijden voor 1 punt, je banden zijn wel op! Ja/Nee ')
                        if keuze2G == "Ja":
                            print('De banden kunnen het niet meer, je rechterachterwiel begeeft het! Je eindigt in de grindbak en kan niet meer verder.')

                            print( str(coureurVS) + ''' heeft de race gewonnen en daardoor is hij eerste in het kampioenschap \n
                            Game Over!
                            ''')
                        else:
                            keuze2G == "Nee"
                            print('Je probeert ' + str(coureurVS) + ' achter je te houden, het is nog erg spannend maar jij hebt nieuwere banden als ' + str(coureurVS) + ' en je rijdt in de laatste sector van hem vandaan')

                            print('Gefeliciteerd, jij hebt de Dutch GP 2021 gewonnen!')

                else:
                    keuze2E2 == "Doorrijden"
                    print('Je banden zijn op, je raakt weer posities kwijt')

                    keuze2E2 = input('Doordat je geen banden hebt gewisseld gaan je banden eraan, wil je je posities behouden of wil zachter gaan rijden en de zekerheid hebben dat je de finish lijn haalt? ')
                    if keuze2E2 == "Behouden":

                        print('''Doordat je posities wilt behouden zijn je banden eraan gegaan en daardoor heb je klapband gehad, je bent uit de race \n
                        Game Over!
                        ''')
                    else:
                        keuze2E2 == "Zekerheid"
                        print('Je hebt gekozen om zachter te gaan rijden zodat je de race wel finisht')

                        print('Dat was een goede keuze, je hebt de race gefinisht, niet op het podium. Maar je bent op de 13e plek geëindigd, niet optimaal maar je hebt de race gefinisht')

            else:
                keuze2D == "Geen"
                print('Je douwt ' + str(coureurTeam) + ' van de baan af, ' + str(coureurTeam) + ' botst tegen de muur aan en verliest zijn voor vleugen. \nJe krijgt aan het einde van de race 10 seconden straf!')

                print('''Je eindigt als 1ste maar daar komen nog 10 seconden tijdstraf bij, je bent 3e geworden \n
                Game Over!
                ''')
    
    else:
        keuze1B == "Nee"
        print(str(coureurVS) + ' gaat aan kop door de bochten')
        
        keuze2B = input('Je rijdt nog steeds heel dicht achter ' + str(coureurVS) + ', jullie komen naast elkaar af denderen op bocht 11. Jij zit aan de rechterkant. ' + str(coureurVS) + ' probeert aan de linker kant voorbij te komen maar word in het grind geduwd door jouw. Geef je de positie gelijk terug of rijd je verder? Ja/Nee ')
        if keuze2B == "Ja":
            print('Je geeft netjes je positie terug, op naar het rechte stuk!')

            print('Word vervolgd!')

        else:
            keuze2B == "Nee"
            print('Je geeft de plek niet terug aan ' + str(coureurVS) + ', je krijgt 10 seconden straf')

            print('Je bent 4e geindigd!')
          
else:
    keuze1A == "Uitremmen"
    print('Je bent tegen ' + str(coureurVS) + ' aangereden! Je licht uit de race!')
    print('Game Over!')