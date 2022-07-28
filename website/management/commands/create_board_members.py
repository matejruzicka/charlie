from django.core.management.base import BaseCommand

from website.models import BoardMember, File


class Command(BaseCommand):
    help = "This command does this and that"

    def handle(self, *args, **options):
        BoardMember.objects.all().delete()
        
        kuba_text = "Starám se povětšinou o organizační stránku událostí a výslovně i Night Out každý třetí čtvrtek" \
                    " v měsíci. <br>Kromě toho funguji díky svým vlasům a výšce i jako orientační bod, pokud nás " \
                    "někdo nemůže najít :)"
        kuba = BoardMember(name="Jakub Šváb", title="Prezident", pronouns="Mužské", medallion=kuba_text,
                photo="charlie/static/sm_Kuba.png", email="prezident@spolekcharlie.cz",
                           email2="jakub.svab@email.cz")
        kuba.save()

        patrik_text = "V Charlie se starám o PR záležitosti a společně s Michalem spravuji naše sociální sítě. Každý " \
                      "třetí čtvrtek organizuji NightOut!, akci pro erasmáky a queer expaty. <br> Mimo Charlie jsem " \
                      "studentem sociologie, milovníkem tance, queer umění a kofeinu. Nebojte se mnou dát do řeči na " \
                      "jedné z našich akcích, nebo na sociálních sítích. A v rámci oficiálních záležitostí mě prosím " \
                      "kontaktujte přes email."
        patrik = BoardMember(name="Patrik Korda", title="Víceprezident", pronouns="Mužské", medallion=patrik_text,
                             photo="charlie/static/sm_Patrik.jpeg",
                             email="viceprezident@spolekcharlie.cz")
        patrik.save()

        adam_text = ""
        adam = BoardMember(name="Adam Urbánek", title="Tajemnik", pronouns="Mužské", medallion=adam_text,
                           photo="charlie/static/sm_Adam.jpeg", email="tajemnik@spolekcharlie.cz")
        adam.save()

        matyas_text = "Ahoj. Já se jako pokladník starám o finance spolku. <br/>Na setkání chodím poměrně často, " \
                      "jsem přátelský a nekoušu.<br/>Vždy se rád seznámím s někým novým."
        matyas = BoardMember(name="Matyáš Medek", title="Pokladník", pronouns="Mužské", medallion=matyas_text,
                             photo="charlie/static/sm_Matyas.png", email="pokladnik@spolekcharlie.cz")
        matyas.save()

        regine_text = "Jsem Regine, spravuju akce a příležitostně pořádám výlety. Mimo spolek se věnuju skolně " \
                      "imunologii a zajmově udržitelnému rozvoji. Čas od času i něco píšu, ať už básničky, " \
                      "wikihesla, nebo spolkový magazín. Mluvit se mnou jde o všem od pečení po klonování myší. " \
                      "Až se nad Akademií objeví duhový hřib, asi se mi něco nepovedlo, to nic.<br> Erasmus? I can " \
                      "speak English y hablo español."
        regine = BoardMember(name="Regine Novotná", title="Řadový člen", pronouns="Ženské", medallion=regine_text,
                             photo="charlie/static/sm_Regine.jpeg", email="",
                             email2="")
        regine.save()

        matej_text = ""
        matej = BoardMember(name="Matěj Evans", title="Řadový člen", pronouns="Mužské", medallion=matej_text,
                            photo="charlie/static/sm_Matej.jpeg", email="iam.matejevans@gmail.com",
                            email2="")
        matej.save()

        michal_text = "Čau! Jako člen výboru pomáhám s čím je třeba. Zaměřuji se primárně na sociální sítě a " \
                      "zlepšování komunikace. Jdeš k nám poprvé? Neváhej se na cokoliv zeptat nebo napsat na náš " \
                      "instagram/facebook."
        michal = BoardMember(name="Michal Mikeska", title="Řadový člen", pronouns="Mužské", medallion=michal_text,
                             photo="charlie/static/sm_Michal.jpeg")
        michal.save()
