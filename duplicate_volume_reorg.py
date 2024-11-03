from capdb.models import VolumeMetadata, Reporter, Citation, EditLog

to_suppress_to_keep = [(["32044109582668"], "32044109582650"), (["32044106827413"], "32044132256546"),
(["32044078700051"], "32044057891848"), (["32044078700044"], "NOTALEPH000568"), (["32044133503029"], "Cal4th_062"),
(["32044133501775"], "CalApp4th_247"), (["32044133501924"], "CalApp4th_248"), (["32044133502443"], "CalApp5th_001"),
(["32044078460268"], "32044078460250"), (["32044115951055"], "32044132277138"), (["NOTALEPH000199"], "32044053222204"),
(["32044053222055", "NOTALEPH000151"], "32044053222204"), (["NOTALEPH000174"], "32044053222196"),
(["32044053222063"], "32044061434247"), (["32044103142949"], "32044103142485"), (["32044061434262"], "32044103142345"),
(["32044132264532"], "32044132252065"), (["32044133502849"], "Ga_299"), (["32044133501593"], "GaApp_337"),
(["32044133502435"], "GaApp_338"), (["32044132259607"], "32044106823339"), (["NOTALEPH000019"], "32044078606506"),
(["32044078429487"], "32044078429818"), (["32044110671542"], "32044078429958"), (["32044066099805"], "32044078179223"),
(["NOTALEPH000230"], "32044066099797"), (["32044132282393"], "32044066099888"), (["32044106247190"], "32044066098146"),
(["32044066098013"], "32044132282401"), (["Mass_474"], "32044133502419"), (["32044132272238"], "32044078599628"),
(["32044132272964"], "32044073053548"), (["32044078459179"], "32044078459161"), (["32044078464203"], "32044078463643"),
(["32044078529922"], "32044078453180"), (["NOTALEPH000729"], "32044078453172"), (["32044133501585"], "Mont_384"),
(["32044133502815"], "Mont_385"), (["32044078426087"], "32044078425055"), (["32044078426095"], "32044078425147"),
(["32044078425030"], "32044078426061"), (["32044078425022"], "32044078426079"), (["HL59QV"], "32044078426111"),
(["32044078425212"], "32044078426129"), (["32044078425170"], "32044078426137"), (["32044078428000"], "32044057447146"),
(["32044078430378"], "32044078428125"), (["32044078430394"], "32044057887580"), (["32044078428158"], "32044057887515"),
(["32044057887523"], "32044078428182"), (["32044078428174"], "32044057887655"), (["32044078430543"], "32044078430535"),
(["32044078430584"], "32044078430592"), (["32044110671641"], "32044057885873"), (["32044078609765"], "32044078488194"),
(["32044057898256"], "32044057886038"), (["32044057898249"], "32044078609955"), (["32044062108949"], "32044078468675"),
(["32044062108931"], "32044078468691"), (["32044078468865"], "32044078468873"), (["32044078438199"], "32044057894743"),
(["32044078438124"], "NOTALEPH000740"), (["32044061465241"], "32044057508731"), (["NOTALEPH001362"], "32044057871006"),
(["32044057887390"], "NOTALEPH000238"), (["32044078614005"], "NOTALEPH000239"), (["NOTALEPH000620"], "32044078606498"),
(["NOTALEPH000621"], "NOTALEPH000146"), (["32044057887382"], "32044078606480"), (["32044057887317"], "NOTALEPH000219"),
(["32044078613999"], "NOTALEPH000220"), (["32044057887242"], "NOTALEPH000221"), (["32044057887176"], "NOTALEPH000222"),
(["32044057887101"], "NOTALEPH000223"), (["NOTALEPH000023", "32044038758082"], "32044078606472"),
(["32044078608460"], "NOTALEPH000158"), (["32044057887168"], "NOTALEPH000156"), (["32044078608478"], "32044078606464"),
(["32044057887440"], "NOTALEPH000191"), (["32044057887374"], "NOTALEPH000192"), (["32044057487977"], "32044078608718"),
(["32044057887309"], "NOTALEPH000167"), (["32044057887234"], "NOTALEPH000168"), (["32044057885360"], "NOTALEPH000240"),
(["32044057885469"], "32044078608726"), (["32044078608486"], "NOTALEPH000235"), (["32044057885402"], "NOTALEPH000236"),
(["32044057885394"], "32044078608734"), (["32044057885386"], "NOTALEPH000125"), (["32044057885378"], "NOTALEPH000126"),
(["32044057865651"], "32044078608742"), (["32044057895781"], "NOTALEPH000153"), (["32044057895716"], "NOTALEPH000154"),
(["32044057895641"], "NOTALEPH000155"), (["32044057895575"], "32044078608759"), (["32044078602349"], "NOTALEPH000196"),
(["32044057895500"], "NOTALEPH000197"), (["32044057895567"], "NOTALEPH000198"), (["32044057895633"], "32044078608767"),
(["32044057895708"], "NOTALEPH000177"), (["32044078602331"], "NOTALEPH000178"), (["32044057895773"], "NOTALEPH000179"),
(["32044057895849"], "32044078608775"), (["32044057895831"], "NOTALEPH000057"), (["32044057895823"], "32044078608783"),
(["32044057895815"], "NOTALEPH000224"), (["32044057895799"], "NOTALEPH000225"), (["32044078602570"], "32044078608791"),
(["32044078602588"], "NOTALEPH000218"), (["32044078602596"], "32044078608809"), (["32044057895724"], "NOTALEPH000217"),
(["32044057895732"], "32044078608817"), (["32044078602448"], "NOTALEPH000216"), (["32044057895740"], "32044078608262"),
(["32044057895757"], "NOTALEPH000128"), (["32044057895765"], "NOTALEPH000129"), (["32044057895658"], "32044078608254"),
(["32044078602455"], "NOTALEPH000123"), (["32044078602463"], "NOTALEPH000124"), (["32044078602471"], "32044078608247"),
(["32044057895666"], "NOTALEPH000121"), (["32044057895674"], "NOTALEPH000122"), (["32044057895682"], "32044078608239"),
(["32044057895690"], "NOTALEPH000152"), (["32044078602604"], "32044078608221"), (["32044057895583"], "NOTALEPH000169"),
(["32044057895591"], "32044078608213"), (["32044057895609"], "NOTALEPH000094"), (["32044078602612"], "32044078608205"),
(["32044057895617"], "NOTALEPH000127"), (["32044057895625"], "32044078608197"), (["32044057895518"], "NOTALEPH000208"),
(["32044078602489"], "32044078608189"), (["32044057895559"], "NOTALEPH000215"), (["NOTALEPH000624"], "32044075295188"),
(["32044133503037"], "VI_065"), (["32044143750016"], "VI_066"), (["32044133502393"], "Wn2d_184"),
(["32044133501619"], "WnApp_190"), (["32044133503011"], "WnApp_192"), (["32044057882334"], "32044057889354"),
(["32044078424454"], "32044078424439")]

part_2 = [("NOTALEPH001514", "NOTALEPH001513"), ("NOTALEPH001511", "NOTALEPH001512"), ("NOTALEPH001553", "NOTALEPH001552"),
("NOTALEPH001550", "NOTALEPH001551"), ("NOTALEPH001560", "NOTALEPH001559"), ("NOTALEPH001555", "NOTALEPH001556"),
("NOTALEPH001554", "NOTALEPH001538"), ("NOTALEPH001544", "NOTALEPH001545"), ("NOTALEPH001542", "NOTALEPH001543"),
("NOTALEPH001548", "NOTALEPH001549"), ("NOTALEPH001546", "NOTALEPH001547"), ("NOTALEPH001557", "NOTALEPH001558"),
("NOTALEPH001537", "NOTALEPH001541"), ("NOTALEPH001539", "NOTALEPH001540"), ("NOTALEPH001561", "NOTALEPH001562"),
("NOTALEPH001563", "NOTALEPH001564"), ("NOTALEPH001566", "NOTALEPH001565"), ("NOTALEPH001567", "NOTALEPH001568"),
("NOTALEPH001570", "NOTALEPH001569"), ("NOTALEPH001572", "NOTALEPH001571"), ("NOTALEPH001456", "NOTALEPH001611"),
("NOTALEPH001610", "NOTALEPH001609"), ("NOTALEPH001591", "HNSRZX"), ("NOTALEPH001589", "NOTALEPH001590"),
("NOTALEPH001588", "NOTALEPH001587"), ("NOTALEPH001585", "NOTALEPH001586"), ("NOTALEPH001584", "NOTALEPH001583"),
("NOTALEPH001581", "NOTALEPH001582"), ("NOTALEPH001577", "NOTALEPH001578"), ("NOTALEPH001579", "NOTALEPH001580"),
("NOTALEPH001573", "NOTALEPH001574"), ("NOTALEPH001576", "NOTALEPH001575"), ("NOTALEPH001534", "NOTALEPH001873"),
("NOTALEPH001595", "NOTALEPH001596"), ("NOTALEPH001536", "NOTALEPH001529"), ("NOTALEPH001874", "NOTALEPH001531"),
("NOTALEPH001532", "NOTALEPH001627"), ("NOTALEPH001628", "NOTALEPH001535"), ("NOTALEPH001530", "NOTALEPH001527"),
("NOTALEPH001626", "NOTALEPH001612"), ("NOTALEPH001524", "NOTALEPH001522"), ("NOTALEPH001526", "NOTALEPH001613"),
("NOTALEPH001593", "NOTALEPH001594"), ("32044047008321", "32044047008313"), ("32044047008305", "32044047008297"),
("32044061360228", "32044061360145"), ("32044061360160", "32044061360152"), ("32044061360178", "32044061360186"),
("32044061360194", "32044061360202"), ("32044115616799", "32044115616682"), ("32044137361820", "32044137361838"),
("32044078456720", "32044078456712"), ("32044058748005", "32044058748278"), ("32044056637275", "32044056637416"),
("32044056637556", "32044056637697"), ("32044060562824", "32044060562832"), ("32044060562808", "32044060562816"),
("32044073189995", "32044073189987"), ("32044097148472", "32044097148464"), ("32044073923401", "32044073923468"),
("32044075667998", "32044078011475"), ("32044097148373", "32044097148365"), ("32044088496369", "32044088496377"),
("32044108017237", "32044108017344"), ("32044115790735", "32044115790727"), ("32044061669594", "32044061669602")]

# Should be 4 N.C. / 2 Car. L. Rep. -- though it's not really 4 N.C. any more than the others	5	NOTALEPH000015, 32044057887291

simple_replace = [
    ("NOTALEPH000597", '12'),
    ("NOTALEPH000596", '11'),
    ("NOTALEPH000595", '10'),
    ("NOTALEPH000594", '9'),
    ("NOTALEPH000593", '8'),
    ("NOTALEPH000592", '7'),
    ("NOTALEPH000591", '6'),
    ("NOTALEPH000590", '5'),
    ("NOTALEPH000589", '4'),
    ("NOTALEPH000588", '3'),
    ("HL560V", '2')
]

def main(dry_run="true"):
    with EditLog(description='Fix duplicate volumes').record(dry_run=dry_run != "false"):
        # mark duplicates
        for duplicate_volume in to_suppress_to_keep:
            preferred_volume = VolumeMetadata.objects.get(pk=duplicate_volume[1])
            for suppress_this in duplicate_volume[0]:
                vol = VolumeMetadata.objects.get(pk=suppress_this)
                if dry_run == "false":
                    vol.set_duplicate(preferred_volume)
                print("set_duplicate,%s,%s" % (vol.barcode, preferred_volume.barcode))

        # mark second parts
        for parts in part_2:
            vol_entry_1 = VolumeMetadata.objects.get(pk=parts[0])
            vol_entry_2 = VolumeMetadata.objects.get(pk=parts[1])

            i = 0
            label_1 = ""
            while not label_1.isdigit():
                label_1 = vol_entry_1.page_structures.order_by('-order')[i].label
                i += 1
            label_1 = int(label_1)

            i = 0
            label_2 = ""
            while not label_2.isdigit():
                label_2 = vol_entry_2.page_structures.order_by('-order')[i].label
                i += 1
            label_2 = int(label_2)

            if label_1 > label_2:
                vol_entry_1, vol_entry_2 = vol_entry_2, vol_entry_1
            vol_entry_2.second_part_of = vol_entry_1
            if dry_run == "false":
                vol_entry_2.save()

            print("second_part_of,%s,%s" % (vol_entry_2.barcode, vol_entry_1.barcode))

        # update Wn2d_185
        Wn2d_185 = VolumeMetadata.objects.get(pk="Wn2d_185")
        reporter = Reporter.objects.get(short_name="Wash. 2d")
        if dry_run == "false":
            Wn2d_185.set_reporter(reporter)
        print("set_reporter,%s,%s" % (Wn2d_185.barcode, reporter.pk))

        # update 32044057887291
        nc_vol = VolumeMetadata.objects.get(pk="32044057887291")
        if dry_run == "false":
            nc_vol.set_volume_number("5")
        print("set_volume_number,%s,%s" % (nc_vol.barcode, "5"))

        #update 25 Tex. Supp
        tex_supp = VolumeMetadata.objects.get(pk="32044078588621")
        if dry_run == "false":
            tex_supp.set_volume_number("25 Supp.")
        print("set_volume_number,%s,%s" % (tex_supp.barcode, "25 Supp."))

        for case in tex_supp.case_metadatas.all():
            cite = "25 Tex. Supp. {}".format(case.first_page)
            if dry_run == "false":
                Citation.objects.create(
                    type="parallel",
                    cite=cite,
                    case=case
                )
            print("new_citation,%s,%s" % (tex_supp.barcode, cite))

        # update 32044078699600
        volume = VolumeMetadata.objects.get(pk="32044078699600")
        duplicate_of = VolumeMetadata.objects.get(pk="32044078592631")
        if dry_run == "false":
            volume.set_volume_number('25')
            volume.set_duplicate(duplicate_of)
        print("set_volume_number,%s,%s" % (volume.barcode, '25'))
        print("set_duplicate,%s,%s" % (volume.barcode, duplicate_of.pk))

        # update volume numbers
        for replace in simple_replace:
            vol = VolumeMetadata.objects.get(pk=replace[0])
            if dry_run == "false":
                vol.set_volume_number(replace[1])
            print("set_volume_number,%s,%s" % (vol.barcode, replace[1]))

