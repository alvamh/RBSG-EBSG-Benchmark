from rdflib import URIRef

entity_numbers = [8, 9, 12, 13, 14, 18, 20, 25, 27, 30, 38, 40, 44, 45, 48, 49, 50,
                  57, 60, 64, 72, 73, 76, 78, 81, 85, 89, 92, 93, 95, 99, 151, 153]
property_numbers = [1, 5, 16, 17, 21, 23, 28, 33, 35, 37, 39, 42, 43, 47, 51, 54, 56,
                    58, 66, 68, 70, 71, 74, 82, 86, 87, 90, 94, 97, 98, 147, 148, 150]
class_numbers = [4, 11, 19, 24, 26, 29, 31, 32, 34, 36, 41, 46, 52, 55, 59, 61, 62,
                 65, 67, 69, 77, 79, 80, 83, 88, 91, 96, 100, 141, 144, 146, 149, 152]

signature_dict = {}

#entity + entity:

signature_dict[8] = [URIRef("http://dbpedia.org/resource/Hagar_Wilde"), URIRef("http://dbpedia.org/resource/Fired_Wife")]
signature_dict[9] = [URIRef("http://dbpedia.org/resource/Ludwigsburg_University"), URIRef("http://dbpedia.org/resource/Ludwigsburg")]
signature_dict[12] = [URIRef("http://dbpedia.org/resource/2011_Kor_Royal_Cup"), URIRef("http://dbpedia.org/resource/Chonburi_F.C.")]
signature_dict[13] = [URIRef("http://dbpedia.org/resource/2011_League_of_Ireland_Cup_Final"), URIRef("http://dbpedia.org/resource/Cork_(city)")]
signature_dict[14] = [URIRef("http://dbpedia.org/resource/2011_Sparta_Prague_Open"), URIRef("http://dbpedia.org/resource/Magdaléna_Rybáriková")]
signature_dict[18] = [URIRef("http://dbpedia.org/resource/Burgery_ambush"), URIRef("http://dbpedia.org/resource/Irish_War_of_Independence")]
signature_dict[20] = [URIRef("http://dbpedia.org/resource/Triathlon_at_the_2000_Summer_Olympics_–_Men's"), URIRef("http://dbpedia.org/resource/Simon_Whitfield")]
signature_dict[25] = [URIRef("http://dbpedia.org/resource/Reamer_Barn"), URIRef("http://dbpedia.org/resource/Ohio_State_Route_511")]
signature_dict[27] = [URIRef("http://dbpedia.org/resource/Uelsby"), URIRef("http://dbpedia.org/resource/Schleswig-Flensburg")]
signature_dict[30] = [URIRef("http://dbpedia.org/resource/Yayoidai_Station"), URIRef("http://dbpedia.org/resource/Sagami_Railway_Izumino_Line")]
signature_dict[38] = [URIRef("http://dbpedia.org/resource/Rubus_arizonensis"), URIRef("http://dbpedia.org/resource/Rosaceae")]
signature_dict[40] = [URIRef("http://dbpedia.org/resource/Trachelipus_dimorphus"), URIRef("http://dbpedia.org/resource/Trachelipodidae")]
signature_dict[44] = [URIRef("http://dbpedia.org/resource/Our_Leading_Citizen_(1939_film)"), URIRef("http://dbpedia.org/resource/Alfred_Santell")]
signature_dict[45] = [URIRef("http://dbpedia.org/resource/Simon_(2004_film)"), URIRef("http://dbpedia.org/resource/Marcel_Hensema")]
signature_dict[48] = [URIRef("http://dbpedia.org/resource/Sting_Me"), URIRef("http://dbpedia.org/resource/The_Black_Crowes")]
signature_dict[49] = [URIRef("http://dbpedia.org/resource/The_Crowd_Snores"), URIRef("http://dbpedia.org/resource/Walter_Lantz")]
signature_dict[50] = [URIRef("http://dbpedia.org/resource/Touch_of_Death_(1961_film)"), URIRef("http://dbpedia.org/resource/Johnny_Douglas_(conductor)")]
signature_dict[57] = [URIRef("http://dbpedia.org/resource/Najmadin_Shukr_Rauf"), URIRef("http://dbpedia.org/resource/Iraqi–Kurdish_conflict")]
signature_dict[60] = [URIRef("http://dbpedia.org/resource/William_Anthony_Hughes"), URIRef("http://dbpedia.org/resource/Youngstown,_Ohio")]
signature_dict[64] = [URIRef("http://dbpedia.org/resource/2008_Copa_del_Rey_Final"), URIRef("http://dbpedia.org/resource/Valencia_CF")]
signature_dict[72] = [URIRef("http://dbpedia.org/resource/Jalalia,_Khyber_Pakhtunkhwa"), URIRef("http://dbpedia.org/resource/Khyber_Pakhtunkhwa")]
signature_dict[73] = [URIRef("http://dbpedia.org/resource/Kings_Ripton"), URIRef("http://dbpedia.org/resource/Huntingdonshire")]
signature_dict[76] = [URIRef("http://dbpedia.org/resource/Pinnacle_Mountain_(South_Carolina)"), URIRef("http://dbpedia.org/resource/Blue_Ridge_Mountains")]
signature_dict[78] = [URIRef("http://dbpedia.org/resource/Sauxillanges"), URIRef("http://dbpedia.org/resource/Auvergne_(region)")]
signature_dict[81] = [URIRef("http://dbpedia.org/resource/Amphisbaena_ridleyi"), URIRef("http://dbpedia.org/resource/Amphisbaenidae")]
signature_dict[85] = [URIRef("http://dbpedia.org/resource/Inverted_repeat-lacking_clade"), URIRef("http://dbpedia.org/resource/Rosids")]
signature_dict[89] = [URIRef("http://dbpedia.org/resource/Thaia_saprophytica"), URIRef("http://dbpedia.org/resource/Gunnar_Seidenfaden")]
signature_dict[92] = [URIRef("http://dbpedia.org/resource/Drama_City"), URIRef("http://dbpedia.org/resource/South_Korea")]
signature_dict[93] = [URIRef("http://dbpedia.org/resource/If_(Glasvegas_song)"), URIRef("http://dbpedia.org/resource/Glasvegas")]
signature_dict[95] = [URIRef("http://dbpedia.org/resource/It's_Still_Rock_and_Roll_to_Me"), URIRef("http://dbpedia.org/resource/Billy_Joel")]
signature_dict[99] = [URIRef("http://dbpedia.org/resource/Time_(Dave_Clark_album)"), URIRef("http://dbpedia.org/resource/Capitol_Records")]
signature_dict[151] = [URIRef("http://dbpedia.org/resource/Ayrovo"), URIRef("http://dbpedia.org/resource/Kardzhali_Municipality")]
signature_dict[153] = [URIRef("http://dbpedia.org/resource/Henlow"), URIRef("http://dbpedia.org/resource/Peter_Watts_(cricketer,_born_1938)")]

#entity + property:

signature_dict[1] = [URIRef("http://dbpedia.org/resource/3WAY_FM"), URIRef("http://dbpedia.org/ontology/broadcastArea")]
signature_dict[5] = [URIRef("http://dbpedia.org/resource/Dallas_Keuchel"), URIRef("http://dbpedia.org/ontology/team")]
signature_dict[16] = [URIRef("http://dbpedia.org/resource/Battle_of_Bregalnica"), URIRef("http://dbpedia.org/ontology/commander")]
signature_dict[17] = [URIRef("http://dbpedia.org/resource/Battle_of_Rottofreddo"), URIRef("http://dbpedia.org/ontology/place")]
signature_dict[21] = [URIRef("http://dbpedia.org/resource/Akalwadi"), URIRef("http://dbpedia.org/ontology/timeZone")]
signature_dict[23] = [URIRef("http://dbpedia.org/resource/Kuleh_Bayan"), URIRef("http://dbpedia.org/ontology/isPartOf")]
signature_dict[28] = [URIRef("http://dbpedia.org/resource/Wehlaberg"), URIRef("http://dbpedia.org/ontology/locatedInArea")]
signature_dict[33] = [URIRef("http://dbpedia.org/resource/Eastern_Sumatran_rhinoceros"), URIRef("http://dbpedia.org/ontology/conservationStatus")]
signature_dict[35] = [URIRef("http://dbpedia.org/resource/Lepiota_helveola"), URIRef("http://dbpedia.org/ontology/binomialAuthority")]
signature_dict[37] = [URIRef("http://dbpedia.org/resource/Ovophis"), URIRef("http://dbpedia.org/ontology/genus")]
signature_dict[39] = [URIRef("http://dbpedia.org/resource/Siamese_mud_carp"), URIRef("http://dbpedia.org/ontology/conservationStatusSystem")]
signature_dict[42] = [URIRef("http://dbpedia.org/resource/Hey_Boy_(Teddybears_song)"), URIRef("http://dbpedia.org/ontology/subsequentWork")]
signature_dict[43] = [URIRef("http://dbpedia.org/resource/King_of_the_Mountain_(film)"), URIRef("http://dbpedia.org/ontology/starring")]
signature_dict[47] = [URIRef("http://dbpedia.org/resource/Sky_(Faye_Wong_album)"), URIRef("http://dbpedia.org/ontology/genre")]
signature_dict[51] = [URIRef("http://dbpedia.org/resource/Ashot_I_of_Iberia"), URIRef("http://dbpedia.org/ontology/successor")]
signature_dict[54] = [URIRef("http://dbpedia.org/resource/Fabrice_Gautrat"), URIRef("http://dbpedia.org/ontology/team")]
signature_dict[56] = [URIRef("http://dbpedia.org/resource/Momchil_Tsvetanov"), URIRef("http://dbpedia.org/ontology/team")]
signature_dict[58] = [URIRef("http://dbpedia.org/resource/Storme_Warren"), URIRef("http://dbpedia.org/ontology/birthPlace")]
signature_dict[66] = [URIRef("http://dbpedia.org/resource/2013_Slovak_Cup_Final"), URIRef("http://dbpedia.org/ontology/team")]
signature_dict[68] = [URIRef("http://dbpedia.org/resource/Battle_of_Cepeda_(1820)"), URIRef("http://dbpedia.org/ontology/commander")]
signature_dict[70] = [URIRef("http://dbpedia.org/resource/Operation_Hump"), URIRef("http://dbpedia.org/ontology/isPartOfMilitaryConflict")]
signature_dict[71] = [URIRef("http://dbpedia.org/resource/Darreh_Dang"), URIRef("http://dbpedia.org/ontology/isPartOf")]
signature_dict[74] = [URIRef("http://dbpedia.org/resource/Kotumachagi"), URIRef("http://dbpedia.org/ontology/isPartOf")]
signature_dict[82] = [URIRef("http://dbpedia.org/resource/Balanites"), URIRef("http://dbpedia.org/ontology/genus")]
signature_dict[86] = [URIRef("http://dbpedia.org/resource/Melaleuca_sheathiana"), URIRef("http://dbpedia.org/ontology/binomialAuthority")]
signature_dict[87] = [URIRef("http://dbpedia.org/resource/Pseudanos_trimaculatus"), URIRef("http://dbpedia.org/ontology/phylum")]
signature_dict[90] = [URIRef("http://dbpedia.org/resource/Trichoscypha_cavalliensis"), URIRef("http://dbpedia.org/ontology/conservationStatusSystem")]
signature_dict[94] = [URIRef("http://dbpedia.org/resource/Intensive_Care_Medicine_(journal)"), URIRef("http://dbpedia.org/ontology/publisher")]
signature_dict[97] = [URIRef("http://dbpedia.org/resource/Rebel_Love_Song"), URIRef("http://dbpedia.org/ontology/genre")]
signature_dict[98] = [URIRef("http://dbpedia.org/resource/Terrorist_Threats"), URIRef("http://dbpedia.org/ontology/producer")]
signature_dict[147] = [URIRef("http://dbpedia.org/resource/Battle_of_Sampur"), URIRef("http://dbpedia.org/ontology/isPartOfMilitaryConflict")]
signature_dict[148] = [URIRef("http://dbpedia.org/resource/Battle_of_Zacatecas_(1914)"), URIRef("http://dbpedia.org/ontology/commander")]
signature_dict[150] = [URIRef("http://dbpedia.org/resource/Raid_on_Griessie"), URIRef("http://dbpedia.org/ontology/combatant")]

#entity + class:

signature_dict[4] = [URIRef("http://dbpedia.org/resource/Anthony_Beaumont-Dark"), URIRef("http://dbpedia.org/class/yago/PeopleFromBirmingham,WestMidlands")]
signature_dict[11] = [URIRef("http://dbpedia.org/resource/2009–10_Swiss_Cup"), URIRef("http://dbpedia.org/ontology/SoccerTournament")]
signature_dict[19] = [URIRef("http://dbpedia.org/resource/Massacre_on_34th_Street"), URIRef("http://dbpedia.org/ontology/WrestlingEvent")]
signature_dict[24] = [URIRef("http://dbpedia.org/resource/Phong_Thạnh_Tây"), URIRef("http://dbpedia.org/ontology/PopulatedPlace")]
signature_dict[26] = [URIRef("http://dbpedia.org/resource/Richmond–Petersburg_Turnpike"), URIRef("http://dbpedia.org/ontology/Road")]
signature_dict[29] = [URIRef("http://dbpedia.org/resource/Wernshausen"), URIRef("http://dbpedia.org/ontology/Location")]
signature_dict[31] = [URIRef("http://dbpedia.org/resource/African_grey_hornbill"), URIRef("http://dbpedia.org/ontology/Bird")]
signature_dict[32] = [URIRef("http://dbpedia.org/resource/Bornean_mountain_ground_squirrel"), URIRef("http://dbpedia.org/ontology/Animal")]
signature_dict[34] = [URIRef("http://dbpedia.org/resource/Enallagma_truncatum"), URIRef("http://dbpedia.org/ontology/Insect")]
signature_dict[36] = [URIRef("http://dbpedia.org/resource/Lygodium_microphyllum"), URIRef("http://dbpedia.org/ontology/Fern")]
signature_dict[41] = [URIRef("http://dbpedia.org/resource/Foppt_den_Dämon!"), URIRef("http://dbpedia.org/ontology/MusicalWork")]
signature_dict[46] = [URIRef("http://dbpedia.org/resource/Sketchy_EP_1"), URIRef("http://dbpedia.org/ontology/Album")]
signature_dict[52] = [URIRef("http://dbpedia.org/resource/Cindy_Mackey"), URIRef("http://dbpedia.org/ontology/GolfPlayer")]
signature_dict[55] = [URIRef("http://dbpedia.org/resource/Hiroshi_Mori_(writer)"), URIRef("http://dbpedia.org/ontology/Manga")]
signature_dict[59] = [URIRef("http://dbpedia.org/resource/Svyatoslav_Tanasov"), URIRef("http://dbpedia.org/ontology/SoccerPlayer")]
signature_dict[61] = [URIRef("http://dbpedia.org/resource/1960_Glover_Trophy"), URIRef("http://dbpedia.org/ontology/FormulaOneRacer")]
signature_dict[62] = [URIRef("http://dbpedia.org/resource/1967_Italian_Grand_Prix"), URIRef("http://dbpedia.org/ontology/FormulaOneTeam")]
signature_dict[65] = [URIRef("http://dbpedia.org/resource/2010_Belgian_Super_Cup"), URIRef("http://dbpedia.org/ontology/FootballMatch")]
signature_dict[67] = [URIRef("http://dbpedia.org/resource/Battle_of_Calicut_(1502)"), URIRef("http://dbpedia.org/class/yago/ViceroysOfPortugueseIndia")]
signature_dict[69] = [URIRef("http://dbpedia.org/resource/Battle_on_the_Elster"), URIRef("http://dbpedia.org/class/yago/BattlesOfTheMiddleAges")]
signature_dict[77] = [URIRef("http://dbpedia.org/resource/Saint-Raphaël,_Var"), URIRef("http://dbpedia.org/ontology/Athlete")]
signature_dict[79] = [URIRef("http://dbpedia.org/resource/Stara_Bučka"), URIRef("http://dbpedia.org/ontology/Settlement")]
signature_dict[80] = [URIRef("http://dbpedia.org/resource/Zarudcze"), URIRef("http://dbpedia.org/ontology/PopulatedPlace")]
signature_dict[83] = [URIRef("http://dbpedia.org/resource/Bryotropha_plantariella"), URIRef("http://dbpedia.org/ontology/Insect")]
signature_dict[88] = [URIRef("http://dbpedia.org/resource/Stemonoporus_laevifolius"), URIRef("http://dbpedia.org/ontology/Plant")]
signature_dict[91] = [URIRef("http://dbpedia.org/resource/392_(album)"), URIRef("http://schema.org/MusicAlbum")]
signature_dict[96] = [URIRef("http://dbpedia.org/resource/Politiken"), URIRef("http://dbpedia.org/ontology/Newspaper")]
signature_dict[100] = [URIRef("http://dbpedia.org/resource/Wide_Awake_Drunk"), URIRef("http://dbpedia.org/ontology/Album")]
signature_dict[141] = [URIRef("http://dbpedia.org/resource/A._Scott_Sloan"), URIRef("http://dbpedia.org/ontology/Politician")]
signature_dict[144] = [URIRef("http://dbpedia.org/resource/Pe_Maung_Tin"), URIRef("http://dbpedia.org/ontology/EthnicGroup")]
signature_dict[146] = [URIRef("http://dbpedia.org/resource/2013_Gulf_Cup_of_Nations"), URIRef("http://dbpedia.org/ontology/SoccerTournament")]
signature_dict[149] = [URIRef("http://dbpedia.org/resource/Convoy_HX_156"), URIRef("http://dbpedia.org/ontology/MilitaryConflict")]
signature_dict[152] = [URIRef("http://dbpedia.org/resource/Fleckistock"), URIRef("http://dbpedia.org/ontology/Mountain")]
