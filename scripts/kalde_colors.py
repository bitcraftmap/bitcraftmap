biome_colors_range = {
	# Biome 0-255		Mask: 0b00000000 00000000 00000000 11111111
	0: [(255, 0, 0), (255, 0, 0)], # RED 000000
	1: [(178, 199, 145), (195, 222, 165)], # CalmForest B2C791 BDD69D
	2: [(118, 123, 108), (139, 147, 123)], # PineWood 767B6C 8B937B
	3: [(165, 165, 165), (255, 255, 255)], # Mountain a5a5ac FFFFFF
	4: [(218, 236, 189), (218, 236, 189)], # BreezyPlains DAECBD
	5: [(182, 145, 92), (207, 173, 101)], # AutumnForest B6915C CFAD65
	6: [(232, 166, 223), (147, 50, 105)], # Tundra E8A6DF 933269
	7: [(222, 217, 200), (241, 236, 218)], # Desert DEE9C8 F1ECD7        DED9C8 #E8E1CD F1ECDA
	8: [(143, 188, 143), (143, 188, 143)], # Swamp 8FBC8F
	9: [(156, 150, 160), (182, 175, 188)], # Canyon 9C96A0 B6AFBC         708090
	10: [(147, 153, 190), (147, 153, 190)], # Ocean 2E6291
	11: [(250, 236, 189), (250, 236, 189)], # SafeMeadows
	12: [(0, 255, 0), (0, 255, 0)], # Cave 00FF00
	13: [(0, 0, 255), (0, 0, 255)], # Jungle 0000FF
	14: [(255, 0, 0), (255, 0, 0)], # Sapwoods FF0000
	
	# Biome Border		Mask: 0b00000000 00000000 11111111 11111111		
	# B1 = a	B2 = b		  0b00000000 00000000 aaaaaaaa bbbbbbbb	
	# Take B2 color range
	# CalmForest Border 256 + B2
	257: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder CalmForest
	258: [(118, 123, 108), (139, 147, 123)], # PineWoodBoder CalmForest
	260: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder CalmForest
	261: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder CalmForest
	262: [(232, 166, 223), (147, 50, 105)], # TundraBorder CalmForest
	263: [(222, 217, 200), (241, 236, 218)], # DesertBorder CalmForest
	264: [(143, 188, 143), (143, 188, 143)], # SwampBorder CalmForest
	265: [(156, 150, 160), (182, 175, 188)], # CanyonBorder CalmForest
	266: [(147, 153, 190), (147, 153, 190)], # OceanBorder CalmForest
	267: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder CalmForest
	268: [(0, 255, 0), (0, 255, 0)], # CaveBorder CalmForest
	269: [(0, 0, 255), (0, 0, 255)], # JungleBorder CalmForest
	270: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder CalmForest

	# PineWood Border 512 + B2
	513: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder PineWood
	514: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder PineWood
	515: [(165, 165, 165), (255, 255, 255)], # MountainBorder PineWood
	516: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder PineWood
	517: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder PineWood
	518: [(232, 166, 223), (147, 50, 105)],  # TundraBorder PineWood
	519: [(222, 217, 200), (241, 236, 218)], # DesertBorder PineWood
	520: [(143, 188, 143), (143, 188, 143)], # SwampBorder PineWood
	521: [(156, 150, 160), (182, 175, 188)], # CanyonBorder PineWood
	522: [(147, 153, 190), (147, 153, 190)], # OceanBorder PineWood
	523: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder PineWood
	524: [(0, 255, 0), (0, 255, 0)], # CaveBorder PineWood
	525: [(0, 0, 255), (0, 0, 255)], # JungleBorder PineWood
	526: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder PineWood

	# Mountain Border 768 + B2
	769: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Mountain
	770: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Mountain
	771: [(165, 165, 165), (255, 255, 255)], # MountainBorder Mountain
	772: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Mountain
	773: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Mountain
	774: [(232, 166, 223), (147, 50, 105)], # TundraBorder Mountain
	775: [(222, 217, 200), (241, 236, 218)], # DesertBorder Mountain
	776: [(143, 188, 143), (143, 188, 143)], # SwampBorder Mountain
	777: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Mountain
	778: [(147, 153, 190), (147, 153, 190)], # OceanBorder Mountain
	779: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Mountain
	780: [(0, 255, 0), (0, 255, 0)], # CaveBorder Mountain
	781: [(0, 0, 255), (0, 0, 255)], # JungleBorder Mountain
	782: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Mountain

	# BreezyPlains Border 1024 + B2
	1025: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder BreezyPlains
	1026: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder BreezyPlains
	1028: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder BreezyPlains
	1029: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder BreezyPlains
	1030: [(232, 166, 223), (147, 50, 105)], # TundraBorder BreezyPlains
	1031: [(222, 217, 200), (241, 236, 218)], # DesertBorder BreezyPlains
	1032: [(143, 188, 143), (143, 188, 143)], # SwampBorder BreezyPlains
	1033: [(156, 150, 160), (182, 175, 188)], # CanyonBorder BreezyPlains
	1034: [(147, 153, 190), (147, 153, 190)], # OceanBorder BreezyPlains
	1035: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder BreezyPlains
	1036: [(0, 255, 0), (0, 255, 0)], # CaveBorder BreezyPlains
	1037: [(0, 0, 255), (0, 0, 255)], # JungleBorder BreezyPlains
	1038: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder BreezyPlains

	# AutumnForest Border 1280 + B2
	1281: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder AutumnForest
	1282: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder AutumnForest
	1284: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder AutumnForest
	1285: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder AutumnForest
	1286: [(232, 166, 223), (147, 50, 105)], # TundraBorder AutumnForest
	1287: [(222, 217, 200), (241, 236, 218)], # DesertBorder AutumnForest
	1288: [(143, 188, 143), (143, 188, 143)], # SwampBorder AutumnForest
	1289: [(156, 150, 160), (182, 175, 188)], # CanyonBorder AutumnForest
	1290: [(147, 153, 190), (147, 153, 190)], # OceanBorder AutumnForest
	1291: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder AutumnForest
	1292: [(0, 255, 0), (0, 255, 0)], # CaveBorder AutumnForest
	1293: [(0, 0, 255), (0, 0, 255)], # JungleBorder AutumnForest
	1294: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder AutumnForest

	# Tundra Border 1536 + B2
	1537: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Tundra
	1538: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Tundra
	1540: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Tundra
	1541: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Tundra
	1542: [(232, 166, 223), (147, 50, 105)], # TundraBorder Tundra
	1543: [(222, 217, 200), (241, 236, 218)], # DesertBorder Tundra
	1544: [(143, 188, 143), (143, 188, 143)], # SwampBorder Tundra
	1545: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Tundra
	1546: [(147, 153, 190), (147, 153, 190)], # OceanBorder Tundra
	1547: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Tundra
	1548: [(0, 255, 0), (0, 255, 0)], # CaveBorder Tundra
	1549: [(0, 0, 255), (0, 0, 255)], # JungleBorder Tundra
	1550: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Tundra

	# Canyon Border 2304 + B2
	2305: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Canyon 
	2306: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Canyon
	2308: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Canyon
	2309: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Canyon
	2310: [(232, 166, 223), (147, 50, 105)], # TundraBorder Canyon
	2311: [(222, 217, 200), (241, 236, 218)], # DesertBorder Canyon
	2312: [(143, 188, 143), (143, 188, 143)], # SwampBorder Canyon
	2313: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Canyon
	2314: [(147, 153, 190), (147, 153, 190)], # OceanBorder Canyon
	2315: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Canyon
	2316: [(0, 255, 0), (0, 255, 0)], # CaveBorder Canyon
	2317: [(0, 0, 255), (0, 0, 255)], # JungleBorder Canyon
	2318: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Canyon

	# Ocean Border 2560 + B2
	2561: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Ocean
	2562: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Ocean
	2564: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Ocean
	2565: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Ocean
	2566: [(232, 166, 223), (147, 50, 105)], # TundraBorder Ocean
	2567: [(222, 217, 200), (241, 236, 218)], # DesertBorder Ocean
	2568: [(143, 188, 143), (143, 188, 143)], # SwampBorder Ocean
	2569: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Ocean
	2570: [(147, 153, 190), (147, 153, 190)], # OceanBorder Ocean
	2571: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Ocean
	2572: [(0, 255, 0), (0, 255, 0)], # CaveBorder Ocean
	2573: [(0, 0, 255), (0, 0, 255)], # JungleBorder Ocean
	2574: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Ocean	

	# SafeMeadows Border 2816 + B2
	2817: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder SafeMeadows
	2818: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder SafeMeadows
	2820: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder SafeMeadows
	2821: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder SafeMeadows
	2822: [(232, 166, 223), (147, 50, 105)], # TundraBorder SafeMeadows
	2823: [(222, 217, 200), (241, 236, 218)], # DesertBorder SafeMeadows
	2824: [(143, 188, 143), (143, 188, 143)], # SwampBorder SafeMeadows
	2825: [(156, 150, 160), (182, 175, 188)], # CanyonBorder SafeMeadows
	2826: [(147, 153, 190), (147, 153, 190)], # OceanBorder SafeMeadows
	2827: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder SafeMeadows
	2828: [(0, 255, 0), (0, 255, 0)], # CaveBorder SafeMeadows
	2829: [(0, 0, 255), (0, 0, 255)], # JungleBorder SafeMeadows
	2830: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder SafeMeadows

	# Cave Border 3072 + B2
	3073: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Cave
	3074: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Cave
	3076: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Cave
	3077: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Cave
	3078: [(232, 166, 223), (147, 50, 105)], # TundraBorder Cave
	3079: [(222, 217, 200), (241, 236, 218)], # DesertBorder Cave
	3080: [(143, 188, 143), (143, 188, 143)], # SwampBorder Cave
	3081: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Cave
	3082: [(147, 153, 190), (147, 153, 190)], # OceanBorder Cave
	3083: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Cave
	3084: [(0, 255, 0), (0, 255, 0)], # CaveBorder Cave
	3085: [(0, 0, 255), (0, 0, 255)], # JungleBorder Cave
	3086: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Cave

	# Jungle Border 3328 + B2
	3329: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Jungle
	3330: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Jungle
	3332: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Jungle
	3333: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Jungle
	3334: [(232, 166, 223), (147, 50, 105)], # TundraBorder Jungle
	3335: [(222, 217, 200), (241, 236, 218)], # DesertBorder Jungle
	3336: [(143, 188, 143), (143, 188, 143)], # SwampBorder Jungle
	3337: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Jungle
	3338: [(147, 153, 190), (147, 153, 190)], # OceanBorder Jungle
	3339: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Jungle
	3340: [(0, 255, 0), (0, 255, 0)], # CaveBorder Jungle
	3341: [(0, 0, 255), (0, 0, 255)], # JungleBorder Jungle
	3342: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Jungle

	# Sapwoods Border 3584 + B2
	3585: [(178, 199, 145), (189, 214, 157)], # CalmForestBorder Sapwoods
	3586: [(118, 123, 108), (139, 147, 123)], # PineWoodBorder Sapwoods
	3588: [(218, 236, 189), (218, 236, 189)], # BreezyPlainsBorder Sapwoods
	3589: [(182, 145, 92), (207, 173, 101)], # AutumnForestBorder Sapwoods
	3590: [(232, 166, 223), (147, 50, 105)], # TundraBorder Sapwoods
	3591: [(222, 217, 200), (241, 236, 218)], # DesertBorder Sapwoods
	3592: [(143, 188, 143), (143, 188, 143)], # SwampBorder Sapwoods
	3593: [(156, 150, 160), (182, 175, 188)], # CanyonBorder Sapwoods
	3594: [(147, 153, 190), (147, 153, 190)], # OceanBorder Sapwoods
	3595: [(250, 236, 189), (250, 236, 189)], # SafeMeadowsBorder Sapwoods
	3596: [(0, 255, 0), (0, 255, 0)], # CaveBorder Sapwoods
	3597: [(0, 0, 255), (0, 0, 255)], # JungleBorder Sapwoods
	3598: [(255, 0, 0), (255, 0, 0)], # SapwoodsBorder Sapwoods

	# ???			Mask: 0b00000000 11111111 11111111 11111111
	# same thing but 3 biomes
	66053: [(184, 184, 184), (184, 184, 184)], # b8b8b8
	66058: [(192, 192, 192), (192, 192, 192)], # c0c0c0
	66562: [(200, 200, 200), (200, 200, 200)], # c8c8c8
	66569: [(200, 200, 200), (200, 200, 200)], # c8c8c8
	66570: [(200, 200, 200), (200, 200, 200)], # c8c8c8
	66573: [(200, 200, 200), (200, 200, 200)], # c8c8c8
	66818: [(208, 208, 208), (208, 208, 208)], # d0d0d0
	66826: [(208, 208, 208), (208, 208, 208)], # d0d0d0
	67850: [(216, 216, 216), (216, 216, 216)], # d8d8d8
	131332: [(224, 224, 224), (224, 224, 224)], # e0e0e0
	131333: [(224, 224, 224), (224, 224, 224)], # e0e0e0
	131338: [(224, 224, 224), (224, 224, 224)], # e0e0e0
	132097: [(232, 232, 232), (232, 232, 232)], # e8e8e8
	132353: [(232, 232, 232), (232, 232, 232)], # e8e8e8
	132618: [(232, 232, 232), (232, 232, 232)], # e8e8e8
	262402: [(240, 240, 240), (240, 240, 240)], # f0f0f0
	262409: [(240, 240, 240), (240, 240, 240)], # f0f0f0
	262410: [(240, 240, 240), (240, 240, 240)], # f0f0f0
	262657: [(240, 240, 240), (240, 240, 240)], # f0f0f0
	264449: [(240, 240, 240), (240, 240, 240)], # f0f0f0
	327938: [(248, 248, 248), (248, 248, 248)], # f8f8f8
	327946: [(248, 248, 248), (248, 248, 248)], # f8f8f8
	328193: [(248, 248, 248), (248, 248, 248)], # f8f8f8
	393738: [(255, 255, 255), (255, 255, 255)], # ffffff
	590090: [(255, 0, 0), (255, 0, 0)] # ff0000
}