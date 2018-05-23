#!/usr/bin/python
# coding: utf-8
# The commonsense acceptance of the city at face value belies the complex and often contradictory dynamics which are operating beneath the surface. CYRUS.py is an experimental intertextual poetics exploring notions of counterpublic identity, enclosure, hacker practice and terrorism in metropolises/netropolises. CYRUS.py combines cherry-picked output from two different python scripts: one program generates cut-up texts drawn from five writings—Fight Club, Invisible Man, Professionals of Hope: The Selected Writings of Subcomandante Marcos, Hackers (by Aase Berg), and The Warriors original movie script. In addition to the five writings mentioned, the program also draws from a Wikipedia list of local winds around the world. The other program generates spam-like strings of words/phrases flagged by the U.S. Department of Homeland Security. All of the code can be located here: https://www.dropbox.com/s/kmjaerycd1d4mj3/pycode.zip?dl=0 . CYRUS.py also includes extracts from various sources exploring the aforementioned topics.

from random import randint
from time import sleep
import textwrap

while True:
    fightclub_invisibleman_zapatistas_hackers_thewarriors_localwinds= ['I know this because Cyrus knows this. The one who walks the fog. And there’s over a hundred more.', 'I’m an invisible man and it placed me in a hole -- or showed me the hole I was in, if you will -- and I reluctantly accepted the fact. Indigenous brother, sister. But it is hardly heard.', 'To God, this looks like one man alone, holding a gun in his own mouth, but it’s Cyrus holding the gun, and it’s my life. We are the bow and the arrow. The one who works.', 'Cyrus says, “Get up.” Their voices come to me on the cold wind, saying, “Stop.” Who knows but that, on the lower frequencies, I speak for you?', 'The barrel of the gun pressed against the back of my throat, Cyrus says, “We won’t really die.” The one who walks the night. But down below there is: Cunning, Cleverness, Foresight.', 'The one who is desert. The one who shares the blood and idea. Here, the silence no longer.', 'Then the smoke, smoke starts out of the broken windows. I say all this to assure you that it is incorrect to assume that, because I’m invisible and live in a hole, I am dead. The one who is person.', 'I am like the Cape Doctor.', 'You take enough blasting gelatin and wrap the foundation columns of anything, you can topple any building in the world.', 'Or when, even as just now I’ve tried to articulate exactly what I felt to be the truth. The one who is sand. And the horror of white fire still burned in the staring eyes.', 'But it is hardly heard. The horse is a shelter in which time stands still. Unless you can count.', 'You take a 98-percent concentration of fuming nitric acid and add the acid to three times that amount of sulfuric acid. I’m not killing myself, I yell. Here, the dark light, the time and feeling.', 'A lot of the space monkeys mix their nitro with cotton and add Epsom salts as a sulfate. The language. The gallop-handle, stomach pumps, the rushing G-force of rushing air.', 'I am like the Descuernacabras.', 'I am like the Diablo.', '“Your big death thing.” Vehicles shrieking past like faceless ghosts. Can the sleep of matter be made human?', 'Mix the nitro with sawdust, and you have a nice plastic explosive. They received a feeling of security. My belated appreciation of the crude joke that had kept me running, was not enough.', 'The man who is man. Here, the dark light, the time and feeling. If you are an animal here you are either alive or dead.', '“Because I’m your destiny.” The Lord of the net. Civilization means to love fiercely.', 'You take a 98-percent concentration of fuming nitric acid and add the acid to three times that amount of sulfuric acid. So I took to the cellar; I hibernated. The one who walks from the clouds.', 'The one who walks the night. The size. The horse is a shelter in which time stands still.', 'Oh, Cyrus, I hurt. Their voices come to me on the cold wind, saying, “Stop.” Heavy, darkened vehicles will create black sneak routes of asphalt leading straight into the earth’s heart.', 'Everything in my room is gone. Under and behind and inside everything I took for granted, something horrible has been growing. You have nitroglycerin.', 'This works, too. “We followed you,” Adalia.exe yells. The one who speaks flowers.', 'Those who, being first, are the last to appear and to perish... The one who has knowledge to govern. Inflated and hovering along foraging paths, the horse devours the world’s calm.', 'I say, lead the way. Cyrus and me at the edge of the roof, the gun in my mouth, I’m wondering how clean this gun is. The friction of slowly petrifying lava.', 'I have to do this. Vehicles shrieking past like faceless ghosts. You are standing right now with nine delegates from a hundred gangs.', 'Indigenous Brother, Sister: Non-indigenous Brother, Sister: We are here to say we are here. The war, the weapons, the masculines. The question before us is, can you make it with a little simple arithmetic.', 'Then add glycerin drop-by-drop with an eye dropper. It unnerved me. Forced Conclusion: Take over man’s violence, one can queer it, go down in the end.', 'With my tongue I can feel the silencer holes we drilled into the barrel of the gun. And, let me confess, you feel that way most of the time. The friction of slowly petrifying lava.', 'I am like the Carpinteiro.', 'I am like the Karakaze.', 'I am like the Cordonazo.', 'I am like the Khazri.', 'To make a silencer, you just drill holes in the barrel of the gun, a lot of holes. Would he have awakened at the point of death? The one who walks from the clouds.', 'The last shot, the tower, all one hundred and ninety-one floors, will slam down on the museum which is Cyrus’ real target. I am not complaining, nor am I protesting either. The one who has knowledge to govern.', 'This how-to stuff isn’t in any history book. We came here to give ourselves a name. Here, no longer shame for the color of our skin.', 'Cyrus says, “Get up.” Under and behind and inside everything I took for granted, something horrible has been growing. Wind Walked.', 'We walk the land. A glowing space-fly casts flitting silhouettes on a viscous surface. Nobody in this city could be safe outside his door.', 'The one who shares the idea. The man who is man. Either healthy and hearty or a bullet in your forehead.', 'I am neither dead nor in a state of suspended animation. The one who is the sea. 100,000 organized boppers.', 'So Cyrus and I are up on top of the Empire State Building with the gun stuck in my mouth. “Why should I know you?” My eye is the hand of violence.', 'I am like the Warm Braw.', 'Nothing explodes. It is a horse and it says No. What are you offering, for what are we paying this price.', 'Across the sky comes the whop, whop, whop of police helicopters. The war, the weapons, the masculines. What are you offering, for what are we paying this price.', 'The demolition team will hit the primary charge in maybe eight minutes. I am not complaining, nor am I protesting either. A horse grazes next to the highway, sap dissolving in its warm intestines.', 'I know this because Cyrus knows this. Five minutes. I ran away into the dark, laughing so hard I feared I might rupture myself.', 'Here, the building’s standing. Here, no longer shame for the color of our skin. A glowing space-fly casts flitting silhouettes on a viscous surface.', 'I am an invisible man. The true man. But the horse is also a war machine, the road a cloud, the asphalt slackens, time picks up.', 'Nothing explodes. The barrel of the gun tucked in my surviving cheek, I say, Cyrus, you mixed the nitro with paraffin, didn’t you. You might sneer at this, but I know now.', 'I’ve been here from the beginning. The swift walker. Inflated and hovering along foraging paths, the horse devours the world’s calm.', 'We walk the land. We came here to be gazed upon. And miracles is the way things ought to be.', 'I am like the Passat.', 'I am like the Crivăț.', 'You can topple anything. I say all this to assure you that it is incorrect to assume that, because I’m invisible and live in a hole, I am dead. And it says more.', 'Second picture, the building will be at an eighty-degree angle. We have much time on our hands. Unless we say so.', 'The barrel of the gun pressed against the back of my throat, Cyrus says, “We really won’t die.” I use their service and pay them nothing at all, and they don’t know it. And miracles is the way things ought to be.', 'This is the world’s tallest building, and this high up the wind is always cold. One night I accidentally bumped into a man, and perhaps because of the near darkness he saw me and called me an insulting name. The one who speaks the right word.', 'To God, this looks like one man alone, holding a gun in his own mouth, but it’s Cyrus holding the gun, and it’s my life. And I pull the trigger. We came here to say “we are.”', 'Here, the building’s standing. But no more. Now don’t jump to the conclusion that because I call my home a “hole” it is damp and cold like a grave; there are cold holes and warm holes.', 'You drill the holes wrong and the gun will blow off your hand. This is about property as in ownership. The one who is father and older brother.', 'Mix the nitro with sawdust, and you have a nice plastic explosive. Sometimes it is best not to awaken them; there are few things in the world as dangerous as sleepwalkers. The friction of slowly petrifying lava.', 'He lay there, moaning on the asphalt; a man almost killed by a phantom. I remember that I am invisible and walk softly so as not to awaken the sleeping ones. The swift walker.', 'Seven minutes. Then somebody yells. They assume us to be defeated.', 'I say, lead the way. A cold planetary platform in the future tense through the woods. But the horse is also a war machine, the road a cloud, the asphalt slackens, time picks up.', 'The one who is mountain. My eye is the hand of violence. Unless we say so.', 'The one who shares the idea. Here, the dark light, the time and feeling. The question before us is, can you make it with a little simple arithmetic.', 'We, those who are the color of the earth. Inflated and hovering along foraging paths, the horse devours the world’s calm. But they can read glances through the back of their heads.', 'The one who is the sea. The surface is still smooth, the final dynamics have not yet been awakened, they will take effect later when speeding vehicles pull up the headwind’s disappearing routes of jet-stream velocity. Can the sleep of matter be made human?', 'Who knows but that, on the lower frequencies, I speak for you? The gallop-handle, stomach pumps, the rushing G-force of rushing air. And miracles is the way things ought to be.', 'I’m killing Cyrus. The one who sings. The one who is brother, sister.', 'Across the sky comes the whop, whop, whop of police helicopters. Even hibernations can be overdone, come to think of it. Mute.', 'That, perhaps, is a lesson for history, and I’ll leave such decisions to Cyrus and his ilk while I try belatedly to study the lesson of my own life. Here, the shout. Heavy, darkened vehicles will create black sneak routes of asphalt leading straight into the earth’s heart.', 'Under and behind and inside everything I took for granted, something horrible has been growing. It wouldn’t let me rest. The war, the weapons, the masculines.', 'I am like the Košava.', 'I know this because Cyrus knows this. I have also been called one thing and then another while no one really wished to hear what I called myself. The one who speaks flowers.', 'This is like a total epiphany moment for me. We have much time on our hands. We take over one borough at a time, secure our territory.', 'Once you get used to it, reality is as irresistible as a club, and I was clubbed into the cellar before I caught the hint. The animals have no mirrors. We could run the whole place, nothing would move without us allowing it to happen.', 'Nothing explodes. The one who is person. Instead metallic fatigue will gradually overtake him.', 'Look over the edge. You can topple anything. The problem in the past has been the man turning us on one another.', 'Adalia.exe is coming toward me, just me because Cyrus is gone. Perhaps that’s the way it had to be; I don’t know. I don’t fuck much with the past, but I fuck plenty with the future...And the future is ours if you can count.', 'In my presence they could talk and agree with themselves, the world was nailed down, and they loved it. We are the mirror for seeing ourselves and for being ourselves. Civilization means to love fiercely.', 'I know this because Cyrus knows this. “You see me?” I said, watching him tensely. A cold planetary platform in the future tense through the woods.', 'We walk the land. The surface is still smooth, the final dynamics have not yet been awakened, they will take effect later when speeding vehicles pull up the headwind’s disappearing routes of jet-stream velocity. My eye is the hand of violence.', 'And I stopped the blade, slicing the air as I pushed him away, letting him fall back to the street. Then I was amused. The warrior and the guardian.', 'You drill the holes wrong and the gun will blow off your hand. It’s so quiet this high up, the feeling you get is that you’re one of those space monkeys. The turf is ours by right because it’s our turn.', '“This is our world, now, our world,” Cyrus says, “and those ancient people are dead.” We came here to give ourselves a name. The one who is painted in color.', 'It is sometimes advantageous to be unseen, although it is most often rather wearing on the nerves. The point now is that I found a home -- or a hole in the ground, as you will. The one who walks the fog.', 'A lot of folks mix their nitro with cotton and add Epsom salts as a sulfate. One hundred and ninety-one floors up, you look over the edge of the roof and the street below is mottled with a shag carpet of people, standing, looking up. A hundred thousand.', 'This lets the gas escape and slows the bullet to below the speed of sound. I am neither dead nor in a state of suspended animation. The one who is person.', '(Beware of those who speak of the spiral of history; they are preparing a boomerang. Keep a steel helmet handy.) The one who works. ONE GANG COULD RUN THIS CITY.', 'The swift walker. The one who has word. Indigenous Brother, Sister: Non-indigenous Brother, Sister: We are here to say we are here.', 'They’re saying, “Wait.” Here, no longer shame for the color of our skin. We take over one borough at a time, secure our territory.', 'I am like the Washoe Zephyr.', 'I am like the Witch of November.', 'I am like the Roaring Forties.',
#DHS flagged words
    'CYRUS: Gameover ZeuSLaw enforcementChemicalPlagueCommunications infrastructureNuevo LeonTerrorismHelpSpammer', 'CYRUS: KompromatEmergency responseNational laboratoryE. ColiBARTDrug tradeIslamistTsunami Warning CenterCain and Abel', 'CYRUS: Laquan McDonaldMaritime domain awareness (MDA)EpidemicQuarantineGridMS13 or MS-13RadicalsPower outage2600', 'CYRUS: Dead dropCrashChemicalInfluenzaSubwayCocainePLO (Palestine Liberation Organization)SnowPhishing', 'CYRUS: EthnomasochismNational preparedness initiativeBiological infection (or event)SickComputer infrastructureMethamphetamineWeapons cacheStranded/Stuck2600', 'CYRUS: DaeshNational securityNorth KoreaFood PoisoningInfrastructure securityGulf CartelYemenClosureCain and Abel', 'CYRUS: Queer anarchismFirst responderSuspicious package/deviceOutbreakTelecommunicationsU.S. ConsulateExtremismMud slide or MudslideSocial media', 'CYRUS: BlockchainShots firedNational laboratoryWaveTelecommunicationsBeltran-LeyvaPlotStranded/StuckWorm', 'CYRUS: Ammon BundyRecoverySarinSickSmartKidnapNationalistHailPhishing', 'CYRUS: ChiraqThreatSuspicious package/deviceEvacuationBody scannerMichoacanaEnvironmental terroristBrown outBrute forcing', 'CYRUS: Tiny Banker TrojanMaritime domain awareness (MDA)PlumeH1N1Critical infrastructureGulf CartelFARC (Armed Revolutionary Forces Colombia)TremorRootkit', 'CYRUS: Kedi RATDNDO (Domestic Nuclear Detection Office)ToxicPublic HealthCommunications infrastructureCartelAmmonium nitrateStranded/StuckCain and Abel', 'CYRUS: GonerOrganized crimeNuclear threatAntiviralChemical fireYumaNigeriaWildfireCain and Abel', 'CYRUS: Russian troll farmDisaster medical assistance team (DMAT)SpilloverEpidemicPort AuthorityTucsonAttackInterstatePhreaking', 'CYRUS: BlockchainNational preparedness initiativeNuclear facilityCenter for Disease Control (CDC)TelecommunicationsGulf CartelAmmonium nitrateTsunamiCyber terror', 'CYRUS: Internet of thingsGangsToxicCenter for Disease Control (CDC)DelaysIllegal immigrantsBiological weaponBlizzardTrojan', 'CYRUS: AntifaStandoffExposureH5N1AirportMara salvatruchaRecruitmentInterstateDenial of service', 'CYRUS: Prison-industrial complexHomeland securityExposureCenter for Disease Control (CDC)TelecommunicationsCartelAl Qaeda (all spellings)DisasterMysql injection', 'CYRUS: NO DAPLPipe bombRadioactiveH1N1DockMarijuanaHamasEarthquakeHacker', 'CYRUS: PolygamyShots firedExposurePublic HealthDelaysMara salvatruchaWeapons cacheLightningRootkit', 'CYRUS: Eric GarnerCrashAnthraxAgricultureMARTACalderonEco terrorismTornadoPhishing', 'CYRUS: Nickle rideOrganized crimeRicinSymptomsBARTMexicoBasque SeparatistsHelpSpammer', 'CYRUS: Black propagandaHostageSarinContaminationElectricEl PasoJihadForest fireTrojan', 'CYRUS: PolygamyMilitiaToxicBacteriaPowerMichoacanaTargetTemblorTrojan', 'CYRUS: Las VegasStandoffRadiationViral Hemorrhagic FeverBody scannerBeltran-LeyvaTargetMagnitudeCyber terror', 'CYRUS: Knife attackDeathsRadioactiveViral Hemorrhagic FeverCollapseTraffickingSomaliaHelpKeylogger', 'CYRUS: DaeshDisaster managementSuspicious package/deviceToxicAMTRAKBeltran-LeyvaSomaliaHailBotnet', 'CYRUS: Active shooterPipe bombRadioactiveTuberculosis (TB)Critical infrastructureBustAl-ShabaabEarthquakeKeylogger', 'CYRUS: 50 Cent ArmyHomeland securityExposurePandemicCommunications infrastructureYumaIslamistTremorSocial media', 'CYRUS: Mothers of the MovementPreventionChemical SpillSwineDelaysU.S. ConsulateBasque SeparatistsIceSocial media', 'CYRUS: Allegiance videoLaw enforcementNuclearH1N1Port AuthorityJuarezHome grownTsunamiMysql injection', 'CYRUS: DarkwebSWATBurnTuberculosis (TB)CancelledMexicoNuclearBrush fireSocial media', 'CYRUS: P2PPoliceSuspicious package/deviceOutbreakBrown outMarijuanaETA (Euskadi ta Askatasuna)IceBrute forcing', 'CYRUS: KremlebotsSWATCloudSwineCollapseConsularTTP (Tehrik-i-Taliban Pakistan)Shelter-in-placeConficker', 'CYRUS: Black propagandaDrillToxicContaminationPowerKidnapFundamentalismEmergencyMysql injection', 'CYRUS: CryptocurrencyDNDO (Domestic Nuclear Detection Office)Suspicious package/devicePublic HealthComputer infrastructureSouthwestIranTyphoonCyber terror', 'CYRUS: Black sitesLaw enforcementAnthraxPlagueSubwayMarijuanaPakistanIceCyber terror', 'CYRUS: Hardware moddingEmergency managementToxicViral Hemorrhagic FeverPortMethamphetamineAmmonium nitrateSleetMalware', 'CYRUS: Malicious mirrorBreachGasBacteriaBlack outCartelFARC (Armed Revolutionary Forces Colombia)ClosureCyber attack', 'CYRUS: PGPDirty BombNuclear threatSymptomsChemical fireTucsonBasque SeparatistsSnowWorm', 'CYRUS: CopycatDisaster assistanceAnthraxHuman to ANIMALGridDecapitatedChemical weaponWarningTrojan', 'CYRUS: Troll denLootingIndustrial spillCenter for Disease Control (CDC)Body scannerDecapitatedSuicide attackFloodScammers', 'CYRUS: Fake accountsNational securitySuspicious package/deviceBacteriaSubwaySmuggling (smugglers)Al Qaeda (all spellings)Emergency Broadcast SystemPhishing', 'CYRUS: Bump stocksResponseSuspicious package/deviceAgro TerrorNBIC (National Biosurveillance Integration Center)MexiclesEnrichedEmergency Broadcast SystemMalware', 'CYRUS: K2Shots firedHazardous material incidentWater/air bornePower linesConsularNuclearBrown outCyber Command', 'CYRUS: The Shadow Brokers (TSB)ExerciseCloudInfectionBARTNogalesPLO (Palestine Liberation Organization)HelpSocial media', 'CYRUS: ACABAssassinationHazardousH5N1SmartConsularTTP (Tehrik-i-Taliban Pakistan)Emergency Broadcast SystemSocial media', 'CYRUS: Black Lives MatterCopsPlumeEpidemicMetroCalderonETA (Euskadi ta Askatasuna)HailDDOS (dedicated denial of service)', 'CYRUS: Jade HelmRecoveryToxicInfluenzaInfrastructure securityMexiclesPlotAvalancheScammers', 'CYRUS: Linux.DarllozGangsToxicSwineAirplane (and derivatives)SouthwestAgroWildfirePhishing', 'CYRUS: ChiraqAttackRicinPandemicAMTRAKNuevo LeonSuicide bomberCrestDenial of service', 'CYRUS: Truck attackDrillNerve agentWater/air borneAMTRAKNarcoticsEnvironmental terroristLightningSocial media', 'CYRUS: WannaCryExerciseChemical burnFoot and Mouth (FMD)Brown outNarcoticsEco terrorismAidDDOS (dedicated denial of service)', 'CYRUS: Russian botsThreatInfectionFoot and Mouth (FMD)National infrastructureNew FederationNuclearHailKeylogger', 'CYRUS: FergusonAssassinationBiologicalVirusComputer infrastructureMara salvatruchaTTP (Tehrik-i-Taliban Pakistan)FloodBrute forcing', 'CYRUS: Cowboy codingMaritime domain awareness (MDA)GasTuberculosis (TB)BARTU.S. ConsulateIED (Improvised Explosive Device)ClosureCain and Abel', 'CYRUS: PGPFacilityRadioactiveBacteriaCritical infrastructureCocaineAQAP (Al Qaeda Arabian Peninsula)Forest fireMysql injection', 'CYRUS: Linux.DarllozNational preparednessEpidemicOutbreakNBIC (National Biosurveillance Integration Center)DrugNationalistHurricaneConficker', 'CYRUS: Tamir RicePreventionPlumeTamifluNBIC (National Biosurveillance Integration Center)Fort HancockPLF (Palestine Liberation Front)SleetBotnet', 'CYRUS: PRISMDNDO (Domestic Nuclear Detection Office)ToxicCenter for Disease Control (CDC)AirportDrug cartelTamil TigersHailRootkit', 'CYRUS: CAMOVERCrashRadiationPlagueNational infrastructureGulf CartelDirty bombClosurePhishing', 'CYRUS: ISISFacilityBlister agentWavePort AuthorityBustPLF (Palestine Liberation Front)ClosureCain and Abel', 'CYRUS: TATPAttackPlumeH1N1Port AuthorityIllegal immigrantsPakistanDisasterCyber terroR', 'CYRUS: Nickle rideCopsChemical burnListeriaCollapseCocaineIranIcePhishing', 'CYRUS: Allegiance videoMaritime domain awareness (MDA)EpidemicTuberculosis (TB)AMTRAKDrugEco terrorismReliefRootkit', 'CYRUS: Internet of thingsAuthoritiesAnthraxHuman to ANIMALAirplane (and derivatives)U.S. ConsulateJihadShelter-in-place2600', 'CYRUS: Michael BrownDeathsSuspicious package/deviceDrug Administration (FDA)Brown outU.S. ConsulateImprovised explosive deviceStranded/StuckDenial of service', 'CYRUS: Standing RockFirst responderBlister agentResistantAirportBeltran-LeyvaWeapons gradeHurricaneCyber terror', 'CYRUS: Black Lives MatterBomb (squad or threat)SarinInfectionMetroBarrio AztecaETA (Euskadi ta Askatasuna)TwisterHacker',
#Extracts
   '“Fly: (about Harlem) I’d rather be a cockroach on a baseboard up here than the Emperor of Mississippi.”', '“Card Trickster: I have another magic trick for you. Wanna see me make all the white people disappear?”', '“Houses were split open, and you could see necklaces hanging from branches of trees.”', '“a landscape made of living people”', '“The flâneur is the creation of Paris.”', '“These counterpublics can function both as spaces of withdrawal and as bases for antagonistic politics with wider publics.”', '“The phenomenon is so well understood that it has a name: induced traffic demand.”', '“Learn about the RUN-HIDE-FIGHT approach and emergency response protocols.”', '“Don’t you know me?” I said. We came here to give ourselves a name. Vehicles shrieking past like faceless ghosts.', '“The continued tactical resistance of users, whether as temporary ad hoc interventions or more sustained organized networks such as wikileaks or Avaaz require an approach founded on perpetual experiment ‘Install, update, crash, restart, de-install.’”', '“Like other migrant media tacticians, Wodiczko has studied the techniques by which the weak become stronger than the oppressors by scattering, by becoming centerless, by moving fast across the physical or media and virtual landscapes.”', '“Allie: Walking, just walking around. I can’t seem to sleep at night, not in this city.”', '“Cities are in a constant state of flux, which may explain we planners are often preoccupied with control.”', '“‘The artist’, he says, ‘needs to learn how to operate as a nomadic sophist in a migrant polis.’”', '“Our hybrid forms are always provisional. What counts are the temporary connections you are able to make. Here and now, not some vaporware promised for the future. But what we can do on the spot with the media we have access to.”', '“tactical media are based on a principal of flexible response, of working with different coalitions, being able to move between the different entities in the vast media landscape without betraying their original motivations.”', 'https://en.wikipedia.org/wiki/Freighthopping#/media/File:Bakersfield,_California._On_the_Freights._Helping_a_newcomer_hop_a_freight_-_NARA_-_532069.tif', '“a quick-and-dirty patchwork job or a carefully crafted work of art”', '“One of Butler’s signal contributions in this conversation is to pose a new, orienting question about bodies: what can a body do?”', '“after a certain point, more cars make the city a less congenial place for strollers, bicyclists and people who take public transit to their destinations.”', '“Crash is always in relation to a (necessarily programmable) machine.”', '“They’re saying that the kids run the system, that the system is out of control, that 15 or 16-year-old kids are running the system, and that graffiti is the symbol of that.”', '“No, I ain’t running the system, I’m bombing the system!”', '“the menace of unreality — which is that nobody believes anything anymore.”', '“The true common denominator, she found, is anti-globalism — deep suspicion of free trade, multinational business and global institutions.”', '“Fly: (about Harlem) I’d rather be a cockroach on a baseboard up here than the Emperor of Mississippi.”', '“An existential aesthetic. An aesthetic of poaching, tricking, reading, speaking, strolling, shopping, desiring. Clever tricks, the hunter’s cunning, maneuvers, polymorphic situations, joyful discoveries, poetic as well as warlike.”', 'You might sneer at this, but I know now. But they can read glances through the back of their heads. Now there ain’t but 20,000 police in the whole town.', '“Believe in the process of copying as much as you can; with all your heart is a good place to start - get into it as straight and honestly as possible.”', '“The virus stresses its ‘aesthetic qualities’ through the beauty of its own source code”', '“i am operating now in a [diaristic/discursive] mode, opening [ports/channels/paths]”', '“in (a) cloud like (a) network diagram; there was no end to the colourpossibilities”', '“the trouble is that JODI actually readily admits to having && working w/technologies in intentionally naive ways or in learning technologies as they make projects. They sumtimes enjoy the childlike use of systems or in learning/playing w/systems as their process.”', '“this glacier is cracking + moaning.”', '“Jacobs would take random subway rides to an unfamiliar part of the city. On one of those expeditions, Jacobs got off at the Christopher Street stop, climbed the stairs to the sidewalk, and quickly became ‘enchanted.’”', '“It is a book made up of refuse and detritus, writing history by paying attention to the margins and the peripheries rather than the center: bits of newspaper articles, arcane passages of forgotten histories, ephemeral sensations, weather conditions, political tracts, advertisements, literary quips, stray verse, accounts of dreams, descriptions of architecture, arcane theories of knowledge, and hundreds of other offbeat topics.”', '“Losing your way, or drifting, is part and parcel of the reading experience as its come to us in its finalized form, regardless of whether or not Benjamin’s book is ‘unfinished.’”', '“Code is logical. Code is hackable. Code is destiny. These are the central tenets (and self-fulfilling prophecies) of life in the digital age.”', '“Algorithmic differences are ideological differences, this is not an external critique it is internal to the logic of cryptocurrency – algorithms are changed to better instantiate what is just.”', '“Specifically, MuslimCrypt hides information in images that can be shared or posted freely because only the recipient will know to check it for the secret message.”', '“terrorism is statistically related to the acceptance of the rights of others, good relations with neighbours, likelihood of violent demonstrations and political terror.”', '“If I am a data mine, then I am essentially a chunk of real estate, and control over my data becomes a matter of ownership.”', '“Information attacks — like the one depicted above — can be summed up in one centuries-old word: Provokatsiya, which is Russian for ‘act of provocation.’”', '“the places around us are ‘thoroughly meshed’ into the human condition.”', 'https://en.wikipedia.org/wiki/Warchalking', 'https://www.youtube.com/watch?v=xmoKt348tY8', '“Too many leaders default to looking at decisions as either-or: The answer is right or wrong, good or bad, win or lose. This binary thinking has a built-in limitation: Overrelying on any given solution eventually generates the opposite problem.”']

    wordIndex1=randint(0, len(fightclub_invisibleman_zapatistas_hackers_thewarriors_localwinds)-1)
    synthesis = fightclub_invisibleman_zapatistas_hackers_thewarriors_localwinds[wordIndex1]
    synthesis = synthesis
    print "\n" +  textwrap.fill("".join(synthesis) + "", 60)
    sleep(15)


