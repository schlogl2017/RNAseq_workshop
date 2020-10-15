# TITLE: this is a dirty script to compare the list of genes of interest
# for DEG using 2 reps and 3 reps.
# Plus the DE exon ...

# to convert the DE exon names to full name:
# paste a list of genes from the DE exon in here

from collections import defaultdict

differential_expression = """
""".split("\n")
for gene in differential_expression:
	if gene == "geneID": continue
	if gene == "": continue
	original_gene_num = int(gene)
	prefix = "Mca"
	gene_number = "%s%05d" % (prefix, original_gene_num)
	print(gene_number)

reps_3_set = set([])

reps_3 = """Mca06377
Mca06378
Mca23428
Mca19702
Mca20960
Mca26558
Mca25862
Mca25512
Mca27614
Mca19998
Mca28211
Mca21166
Mca19994
Mca19997
Mca19996
Mca19995
Mca26214
Mca03967
Mca06376
Mca19066
Mca19442
Mca18373
Mca18372
Mca23378
Mca15274
Mca22238
Mca27613
Mca16034
Mca24756
Mca28299
Mca26215
Mca20961
Mca18527
Mca25101
Mca24407
Mca19396
Mca14739
Mca24131
Mca25491
Mca25492
Mca26349
Mca20417
Mca19395
Mca22267
Mca26482
Mca19789
Mca26860
Mca26671
Mca03966
Mca25229
Mca22992
Mca24408
Mca24347
Mca18026
Mca25227
Mca25228
Mca00614
Mca18982
Mca12519
Mca23171
Mca00210
Mca07321
Mca14609
Mca14608
Mca10448
Mca13168
Mca20926
Mca28167
Mca22378
Mca23405
Mca25661
Mca19237
Mca19236
Mca19235
Mca14610
Mca14218
Mca19306
Mca27781
Mca11740
Mca16172
Mca19239
Mca13270
Mca18229
Mca13167
Mca26557
Mca28399
Mca20573
Mca22761
Mca17855
Mca25416
Mca04958
Mca27362
Mca07320
Mca08829
Mca16243
Mca13613
Mca20255
Mca22824
Mca19238
Mca25379
Mca23579
Mca20576
Mca20578
Mca19674
Mca19673
Mca19672
Mca16455
Mca26450
Mca11409
Mca19781
Mca19450
Mca16981
Mca20577
Mca07514
Mca20402
Mca21467
Mca28400
Mca13431
Mca03555
Mca26028
Mca16980
Mca20306
Mca25992
Mca25846
Mca16598
Mca20020
Mca09288
Mca19539
Mca17389
Mca27438
Mca18907
Mca21466
Mca15213
Mca16599
Mca18141
Mca18909
Mca19018
Mca16318
Mca26898
Mca06693
Mca06755
Mca26223
Mca27365
Mca02897
Mca01766
Mca16600
Mca23530
Mca03464
Mca04488
Mca26075
Mca11204
Mca12540
Mca11727
Mca03951
Mca17952
Mca15214
Mca11205
Mca27966
Mca14854
Mca03421
Mca22014
Mca22066
Mca25378
Mca26222
Mca20718
Mca13432
Mca25331
Mca01384
Mca04595
Mca22591
Mca23889
Mca28610
Mca04489
Mca17580
Mca02517
Mca28672
Mca00315
Mca19508
Mca27047
Mca22971
Mca26076
Mca25294
Mca22592
Mca24809
Mca19708
Mca27392
Mca07515
Mca07046
Mca18908
Mca16300
Mca27340
Mca10432
Mca04939
Mca28636
Mca26509
Mca07516
Mca14094
Mca25201
Mca07323
Mca17259
Mca16362
Mca05387
Mca00995
Mca22970
Mca15550
Mca11731
Mca09738
Mca18228
Mca21408
Mca24089
Mca20443
Mca04487
Mca01915
Mca23251
Mca06958
Mca23319
Mca07338
Mca12235
Mca02696
Mca10734
Mca20677
Mca28276
Mca07804
Mca17324
Mca21959
Mca21738
Mca12703
Mca25725
Mca27020
Mca06084
Mca09259
Mca00155
Mca07173
Mca18314
Mca07675
Mca23655
Mca23816
Mca16716
Mca03757
Mca23374
Mca19531
Mca05910
Mca18027
Mca27583
Mca03935
Mca20055
Mca18003
Mca25993
Mca22657
Mca25309
Mca19826
Mca28656
Mca22198
Mca12936
Mca07744
Mca16350
Mca15219
Mca17863
Mca23313
Mca19447
Mca22934
Mca01765
Mca24633
Mca07864
Mca27284
Mca23159
Mca00488
Mca22977
Mca21506
Mca16597
Mca11068
Mca12803
Mca25808
Mca09337
Mca25111
Mca14032
Mca14622
Mca04392
Mca15315
Mca15971
Mca19669
Mca13140
Mca06436
Mca27287
Mca15314
Mca16830
Mca07415
Mca04734
Mca14593
Mca12920""".split("\n")

# i dont trust the \n are there which has caused a lack of intersection
for i in reps_3:
    reps_3_set.add(i.rstrip())

de_exon_set = set([])
de_exon = """Mca22307
Mca16239
Mca11202
Mca22735
Mca02319
Mca01056
Mca12616
Mca26363
Mca05018
Mca06437
Mca10218
Mca13137
Mca01668
Mca18305
Mca19140
Mca22154
Mca22496
Mca23515
Mca25150
Mca04356
Mca06667
Mca06949
Mca11449
Mca12389
Mca15133
Mca16961
Mca18349
Mca18443
Mca20065
Mca20608
Mca21001
Mca21367
Mca21841
Mca23105
Mca23837
Mca24262
Mca24597
Mca03688
Mca03920
Mca07566
Mca07685
Mca10172
Mca10267
Mca10643
Mca11267
Mca11639
Mca12586
Mca12615
Mca12705
Mca12775
Mca12886
Mca14103
Mca14119
Mca14278
Mca14736
Mca14852
Mca15400
Mca15438
Mca17770
Mca17871
Mca17894
Mca17944
Mca01818
Mca18643
Mca18740
Mca18795
Mca19914
Mca20679
Mca20681
Mca21133
Mca22687
Mca22902
Mca23491
Mca23891
Mca02414
Mca24216
Mca24398
Mca24554
Mca25650
Mca25821
Mca26348
Mca26751
Mca03275
Mca04451
Mca05750
Mca06436
Mca07383
Mca00756
Mca08409
Mca09229
Mca10091
Mca10130
Mca10182
Mca10282
Mca10323
Mca10518
Mca10614
Mca10616
Mca10640
Mca10681
Mca10742
Mca11053
Mca11384
Mca11411
Mca11488
Mca11491
Mca11620
Mca11737
Mca11791
Mca11813
Mca11976
Mca12153
Mca12394
Mca12438
Mca12721
Mca12811
Mca12852
Mca12861
Mca12889
Mca12936
Mca01300
Mca13009
Mca13301
Mca13382
Mca01364
Mca13681
Mca13865
Mca14033
Mca14060
Mca14061
Mca01409
Mca14313
Mca14572
Mca14655
Mca14933
Mca15036
Mca15324
Mca15905
Mca16246
Mca01630
Mca16301
Mca16317
Mca16429
Mca16807
Mca16932
Mca17114
Mca17299
Mca17310
Mca17389
Mca17435
Mca17556
Mca17813
Mca17883
Mca17925
Mca18059
Mca18516
Mca18590
Mca18742
Mca18948
Mca19409
Mca19428
Mca19571
Mca19638
Mca19682
Mca19871
Mca20263
Mca20444
Mca20502
Mca20619
Mca20733
Mca20752
Mca20754
Mca20951
Mca02106
Mca21265
Mca21368
Mca22029
Mca22041
Mca22288
Mca22375
Mca22500
Mca22592
Mca22658
Mca22757
Mca22893
Mca23002
Mca23091
Mca23145
Mca23840
Mca23901
Mca23924
Mca24003
Mca02406
Mca24086
Mca24494
Mca24673
Mca24691
Mca24932
Mca25189
Mca25521
Mca25677
Mca26257
Mca26512
Mca26629
Mca26709
Mca26775
Mca26840
Mca26863
Mca02719
Mca27397
Mca27642
Mca27853
Mca27931
Mca28002
Mca28164
Mca02834
Mca02943
Mca03191
Mca03358
Mca03464
Mca03910
Mca04445
Mca04473
Mca04476
Mca00449
Mca04642
Mca05015
Mca00514
Mca05616
Mca00057
Mca05751
Mca06162
Mca06275
Mca00634
Mca06643
Mca07580
Mca07621
Mca07628
Mca07633
Mca07702
Mca07786
Mca08264
Mca08403
Mca08412
Mca08413
Mca08422
Mca08769
Mca08774
Mca09055
Mca00909
Mca09125
Mca09137
Mca09177
Mca09315
Mca09481
Mca09517
Mca09617
Mca09664
Mca09975
Mca09998
Mca10116
Mca11159
Mca12343
Mca14832
Mca15064
Mca15182
Mca15825
Mca17398
Mca17730
Mca18406
Mca20048
Mca20476
Mca20541
Mca21428
Mca22176
Mca22865
Mca24524
Mca24806
Mca26494
Mca27259
Mca27632
Mca28020
Mca28573
Mca03260
Mca04341
Mca05897
Mca00604
Mca07222
Mca07564""".split("\n")

reps_2 = """Mca06378
Mca06377
Mca23428
Mca27614
Mca24131
Mca16034
Mca22267
Mca19395
Mca19239
Mca14609
Mca14608
Mca25862
Mca19702
Mca18982
Mca19237
Mca19236
Mca19235
Mca19442
Mca19396
Mca03967
Mca20960
Mca22992
Mca26558
Mca25416
Mca10448
Mca03966
Mca28211
Mca28167
Mca19998
Mca24407
Mca25512
Mca21166
Mca14610
Mca23378
Mca19066
Mca18373
Mca24347
Mca18372
Mca19994
Mca19997
Mca19996
Mca19995
Mca07321
Mca26214
Mca15274
Mca24756
Mca28299
Mca18527
Mca12519
Mca22238
Mca25101
Mca27613
Mca26028
Mca06376
Mca25229
Mca16455
Mca14739
Mca14713
Mca26215
Mca20961
Mca22378
Mca03134
Mca25227
Mca25228
Mca23171
Mca26559
Mca26349
Mca20417
Mca07915
Mca25492
Mca25491
Mca16087
Mca26482
Mca26860
Mca26267
Mca25846
Mca26671
Mca24408
Mca09288
Mca18026
Mca18229
Mca20573
Mca17855
Mca19789
Mca00210
Mca13613
Mca19672
Mca19674
Mca19673
Mca13168
Mca25661
Mca00614
Mca18907
Mca11409
Mca16318
Mca13167
Mca18909
Mca19306
Mca25379
Mca20306
Mca20926
Mca01346
Mca14218
Mca15213
Mca23579
Mca11740
Mca01344
Mca27362
Mca27781
Mca03421
Mca23405
Mca27438
Mca26557
Mca06755
Mca28399
Mca13270
Mca07320
Mca18141
Mca16172
Mca19238
Mca23530
Mca22761
Mca16243
Mca02980
Mca19450
Mca25992
Mca15214
Mca21466
Mca22824
Mca21467
Mca11727
Mca07514
Mca26898
Mca24307
Mca04958
Mca13432
Mca19781
Mca28400
Mca13431
Mca17389
Mca04488
Mca20576
Mca20578
Mca08829
Mca16981
Mca20402
Mca16980
Mca25331
Mca28636
Mca16598
Mca20255
Mca19539
Mca02897
Mca18908
Mca26450
Mca04774
Mca16600
Mca26222
Mca25378
Mca03951
Mca16599
Mca27020
Mca17580
Mca20577
Mca03464
Mca07863
Mca03555
Mca07046
Mca20020
Mca26223
Mca04595
Mca01766
Mca11204
Mca01384
Mca22014
Mca06693
Mca22591
Mca24089
Mca28610
Mca11205
Mca17952
Mca26075
Mca02517
Mca19508
Mca27365
Mca12540
Mca06084
Mca22592
Mca14854
Mca23319
Mca00315
Mca28672
Mca07515
Mca22066
Mca12235
Mca27340
Mca22934
Mca16300
Mca04489
Mca21959
Mca27047
Mca15550
Mca20718
Mca14094
Mca18003
Mca04939
Mca23889
Mca19018
Mca26076
Mca22971
Mca07338
Mca27966
Mca10432
Mca11731
Mca00995
Mca19708
Mca07323
Mca07516
Mca24633
Mca05387
Mca16362
Mca24809
Mca14810
Mca00155
Mca18228
Mca28656
Mca06958
Mca04487
Mca27392
Mca25682
Mca25294
Mca01915
Mca28276
Mca07804
Mca07675
Mca07173
Mca19851
Mca25461
Mca23251
Mca09738
Mca01765
Mca25201
Mca09259
Mca22970
Mca17324
Mca23772
Mca23816
Mca28500
Mca26509
Mca21738
Mca21408
Mca20055
Mca04119
Mca28645
Mca00488
Mca20677
Mca12703
Mca10036
Mca19826
Mca09337
Mca17259
Mca10422
Mca18027
Mca26296
Mca23374
Mca25808
Mca25993
Mca25665
Mca28352
Mca22969
Mca19447
Mca17829
Mca23313
Mca04734
Mca19531
Mca23100
Mca16597
Mca15219
Mca12920
Mca12368
Mca03757
Mca06629
Mca17737
Mca07563
Mca07207
Mca12936
Mca04073
Mca07864
Mca21568
Mca22198
Mca11068
Mca14032
Mca09193
Mca18314
Mca15971
Mca11430
Mca23674
Mca05910
Mca27583
Mca20443
Mca10734
Mca27284
Mca02696
Mca07200
Mca14622
Mca16716
Mca00712
Mca24251
Mca25111
Mca12803
Mca19669
Mca15598
Mca04392
Mca23833
Mca01182
Mca03935
Mca22657
Mca16350
Mca14593
Mca13732
Mca00157
Mca14035
Mca01881
Mca17863
Mca09827
Mca21397
Mca17734""".split("\n")


eff_name_annot =  defaultdict(str)
effectors = """Mca22940	dihydrouridine synthase domain containing protein
Mca23697	fmrfamide-related neuropeptides
Mca05071	PREDICTED: prisilkin-39-like
Mca05072	cuticle isoform x1
Mca23834	endocuticle structural glycoprotein bd-1-like
Mca23918	thaumatin-like protein
Mca24130	repetitive proline-rich cell wall protein 2-like
Mca24190	PREDICTED: uncharacterized protein LOC107164962
Mca00781	PREDICTED: uncharacterized protein LOC100573104
Mca00788	maltase isoform c
Mca24498	glucose dehydrogenase
Mca00802	one cut domain family member 3-like
Mca05338	cuticular protein rr-1 motif 48
Mca05372	ejaculatory bulb-specific protein 3
Mca05377	---NA---
Mca00818	pupal cuticle protein 27-like
Mca24956	serine protease 44-like
Mca25013	cell wall protein awa1-like
Mca00834	growth differentiation factor 8
Mca00119	glucose dehydrogenase
Mca25154	cuticle protein 7-like
Mca05447	cardioactive peptide
Mca00838	low affinity immunoglobulin epsilon fc receptor-like
Mca25466	protein takeout
Mca25670	low quality protein: vacuolar protein sorting-associated protein 62-like
Mca25932	odorant-binding protein partial
Mca05677	mam and ldl-receptor class a domain-containing protein 1-like
Mca05783	venom protease-like
Mca05785	venom protease-like
Mca27192	endocuticle structural glycoprotein bd-1-like
Mca27237	cuticle protein 7-like
Mca06064	trehalase-like
Mca27619	cuticular protein 72 precursor
Mca06105	arylsulfatase b
Mca06115	adhesive plaque matrix
Mca06149	adhesive plaque matrix isoform x1
Mca27991	ejaculatory bulb-specific protein 3
Mca06277	tetra-peptide repeat homeobox protein 1-like
Mca06278	tetra-peptide repeat homeobox protein 1-like
Mca28321	valacyclovir hydrolase-like
Mca06562	cuticle protein
Mca06563	cuticle protein 7-like
Mca06588	protein yellow
Mca06687	myosuppressin
Mca06692	tetra-peptide repeat homeobox protein 1-like
Mca06812	PREDICTED: uncharacterized protein LOC103310813
Mca06815	PREDICTED: uncharacterized protein LOC100576074
Mca06816	PREDICTED: uncharacterized protein LOC103310813
Mca06839	PREDICTED: uncharacterized protein LOC107168144
Mca06864	PREDICTED: uncharacterized protein LOC100164831 isoform X2
Mca06902	venom protease-like
Mca06961	PREDICTED: putative uncharacterized protein DDB_G0282133
Mca06986	agap012355-pa-like protein
Mca06987	pollen-specific leucine-rich repeat extensin-like protein partial
Mca06994	cuticle protein 21
Mca07065	pdgf- and vegf-related factor 1-like precursor
Mca07169	glycoprotein hormone alpha-2
Mca07174	beta-galactosidase-like
Mca07207	serine arginine-rich splicing factor 8-like
Mca07285	non-catalytic module family expn protein
Mca07500	endocuticle structural glycoprotein abd-4-like
Mca07514	rna-binding protein 14-like
Mca07516	hybrid sensor histidine kinase response regulator
Mca07765	allatostatin neuropeptide precursor
Mca07966	os-d-like protein
Mca07973	transcription factor 21
Mca08194	lipase 3-like
Mca01376	serine arginine-rich splicing factor 8-like
Mca08493	---NA---
Mca08518	thaumatin-like protein
Mca08560	udp-glucuronosyltransferase 2c1-like
Mca08609	dna-directed rna polymerase ii subunit rpb1-like
Mca08641	collagen alpha-1 chain-like
Mca08684	peptidyl-prolyl cis-trans isomerase b-like
Mca01472	PREDICTED: uncharacterized protein LOC100573339
Mca08772	aminopeptidase n-like
Mca08790	protein takeout
Mca08810	collagen alpha-2 chain
Mca09072	PREDICTED: uncharacterized protein LOC107163177
Mca09115	protein takeout-like
Mca09213	PREDICTED: uncharacterized protein LOC107164781
Mca09245	eclosion hormone
Mca09259	cuticle precursor
Mca09395	cilia- and flagella-associated protein 57 isoform x1
Mca09475	zinc metalloproteinase nas-13-like
Mca01661	neither inactivation nor afterpotential protein c isoform x1
Mca09662	chorion peroxidase-like
Mca09734	serine proteinase stubble
Mca09743	chemosensory protein
Mca09787	PREDICTED: prisilkin-39-like
Mca09872	septation ring formation family protein
Mca09936	actin-like protein 6a
Mca01756	protein yellow
Mca10028	glucose dehydrogenase
Mca01815	zinc finger protein 512b-like
Mca10507	---NA---
Mca01881	eukaryotic peptide chain release factor gtp-binding subunit-like
Mca01882	sporozoite surface protein 2-like
Mca01883	---NA---
Mca10566	cyclin-dependent kinase inhibitor 1c-like
Mca01905	---NA---
Mca10686	---NA---
Mca10687	collagen alpha-1 chain-like
Mca10724	nose resistant to fluoxetine protein 6-like
Mca01955	cyclin-dependent kinase 8-like
Mca10833	angiotensin-converting enzyme
Mca11052	retrovirus-related pol polyprotein from transposon partial
Mca02006	class e vacuolar protein-sorting machinery protein hse1
Mca11388	neurofilament heavy polypeptide-like
Mca11427	von willebrand factor type egf and pentraxin domain-containing protein 1
Mca11825	glucose dehydrogenase
Mca11838	PREDICTED: uncharacterized protein LOC103310518
Mca11855	cytokine receptor
Mca02134	cuticle protein 7-like
Mca02135	cuticle protein 7-like
Mca02136	cuticle protein 7-like
Mca02137	cuticle protein 7-like
Mca02139	cuticle protein 7-like
Mca02140	cuticle protein 7-like
Mca02141	cuticle protein 7-like
Mca11900	matrix metalloproteinase-14 isoform x2
Mca11975	bifunctional endo- -beta-xylanase -like
Mca12153	prothoracicostatic peptide
Mca12177	probable chitinase 3
Mca12233	thaumatin-like protein
Mca12289	glucose dehydrogenase
Mca12602	collagen alpha-1 chain-like
Mca12634	endocuticle structural glycoprotein bd-2-like
Mca12809	flocculation protein flo11-like
Mca12891	adhesive plaque matrix
Mca13009	glucose dehydrogenase
Mca02375	cg31997- partial
Mca13173	neuroendocrine protein 7b2
Mca13198	fungistatic metabolite
Mca13276	repetitive proline-rich cell wall protein 2-like
Mca13331	cuticle precursor
Mca13558	pro-resilin-like
Mca02473	tachykinins isoform x1
Mca02481	dna ligase 1-like
Mca13758	probable cytochrome p450 6a13
Mca00382	prohormone-4
Mca02531	PREDICTED: uncharacterized protein LOC107165343 isoform X1
Mca14061	histidine-rich glyco
Mca14161	carbonic anhydrase 2-like
Mca02655	---NA---
Mca02656	repetitive proline-rich cell wall protein 2-like
Mca02658	repetitive proline-rich cell wall protein 2-like
Mca14349	protein takeout-like
Mca14350	protein takeout-like
Mca14392	cuticle protein 7-like
Mca14393	cuticle protein 7-like
Mca14553	glycine-rich cell wall structural protein 2- partial
Mca14606	protein yellow-like
Mca14682	ACYPI001887
Mca14686	probable cytochrome p450 6a14
Mca14782	cuticle protein 7-like
Mca02809	beat- isoform a
Mca15064	glycine-rich cell wall structural isoform x1
Mca15421	cuticle protein
Mca02894	larval cuticle protein a2b-like
Mca02896	cuticle protein 7-like
Mca02950	protein yellow
Mca15740	PREDICTED: gelsolin-like
Mca15871	PREDICTED: uncharacterized protein LOC103311148
Mca03039	PREDICTED: uncharacterized protein LOC107165482
Mca16374	lipase 3-like
Mca16466	chitooligosaccharidolytic beta-n-acetylglucosaminidase
Mca16553	larval cuticle protein lcp-17-like
Mca03138	mediator of rna polymerase ii transcription subunit 15-like
Mca00489	membrane-bound alkaline phosphatase-like
Mca03217	---NA---
Mca16980	PREDICTED: uncharacterized protein LOC100164207 isoform X1
Mca03243	tubulointerstitial nephritis antigen-like
Mca17153	caldesmon isoform x1
Mca17157	adenylate kinase 9-like
Mca17244	PREDICTED: uncharacterized protein LOC100163191
Mca17352	cartilage oligomeric matrix protein
Mca17468	endoglucanase 15-like
Mca00514	prickle-like protein partial
Mca03374	mediator of rna polymerase ii transcription subunit 26
Mca03375	cuticle protein 19-like
Mca03376	cuticle protein 7-like
Mca17864	PREDICTED: uncharacterized protein LOC100574363
Mca03428	glucose dehydrogenase
Mca03453	trypsin-1-like
Mca17986	clipa6 protein
Mca03467	adhesive plaque matrix protein isoform x2
Mca03516	cuticle protein 7-like
Mca03517	dna-directed rna polymerase ii subunit rpb1-like
Mca03518	cuticle protein 7-like
Mca03519	cuticle protein 7-like
Mca03520	cuticle protein 7-like
Mca03521	cuticle protein 7-like
Mca03522	cuticle protein 7-like
Mca03523	cuticle protein 7-like
Mca18572	maverick capsid-like
Mca18785	peroxidase-like isoform x2
Mca03652	defense protein hdd11
Mca03661	early nodulin-75
Mca19101	uncharacterized protein LOC100165421 precursor
Mca19159	neuropeptide f
Mca19262	circadian clock-controlled
Mca03804	cuticular protein analogous to peritrophins 3-d1 precursor
Mca19546	venom serine protease-like
Mca00079	---NA---
Mca03900	cellular retinaldehyde binding protein
Mca04010	protein takeout-like
Mca20140	---NA---
Mca04055	cuticle protein 19-like
Mca00616	sheath partial
Mca04067	carotenoid isomerooxygenase isoform x1
Mca00620	ly6 plaur domain-containing protein 6b-like
Mca20639	cuticle protein 7-like
Mca04188	endoplasmic reticulum aminopeptidase 2-like
Mca20840	short-chain dehydrogenase reductase family 16c member 6-like isoform x2
Mca04242	serine protease 44-like
Mca21139	glucose dehydrogenase
Mca21192	adhesin-like protein
Mca21224	carboxypeptidase e-like
Mca22031	endoglucanase 15-like
Mca04628	nose resistant to fluoxetine protein 6-like
Mca22270	protein takeout
Mca22327	atp-dependent dna helicase pif6-like
Mca22401	protein takeout""".split("\n")

# make an effecotr set for comparisons later
effector_set = set([])
for eff in effectors:
        name, annotation = eff.split("\t")
        # assign the annot to a dictionary
        eff_name_annot[name] = annotation.rstrip()
        effector_set.add(name.rstrip())

# i dont trust the \n are there which has caused a lack of intersection
for entry in reps_3:
    reps_3_set.add(entry.rstrip())
    
de_exon_set = set([])
for entry in de_exon:
  de_exon_set.add(entry.rstrip())

reps_2_set = set([])
for entry in reps_2:
    reps_2_set.add(entry.rstrip())

def retrive_annotation(inset, annot_dict):
    """function to tell us the annot of the gene in a given
    set
    take in a set and a dictionary as gene[annot]
    """
    for common_gene in inset:
        annot = eff_name_annot[common_gene]
        print("%s\t%s" % (common_gene, annot))

# compare the sets of names
print("length of DE exon gene set : ", len(de_exon_set))
print("length of DEG reps_3 set : ", len(reps_3))
print("length of DEG reps_2 set : ", len(reps_2))
print("\nDEG 2 reps has this many overlap with DE exon: ",
      len(reps_2_set.intersection(de_exon_set)))

print("DEG 3 reps has this many overlap with DE exon: ",
      len(reps_3_set.intersection(de_exon_set)))

print("DEG 2 reps has this many overlap with 3 reps: ",
      len(reps_2_set.intersection(reps_3_set)))

print("DEG 3 reps has this many overlap with DE exon and 2 reps: ",
      len(reps_3_set.intersection(de_exon_set, reps_2_set)))
gene_common_in_DEexon_DEG = reps_3_set.intersection(de_exon_set)

# lets compare the effector (gene of interest)
print("\nwe have %d effectors in our starting list" % len(effector_set))
effecotr_in_DE_exon = effector_set.intersection(de_exon_set)
print("\n%d effecotrs were found in the DE exon anlaysis" %
      (len(effecotr_in_DE_exon)))
# call a fucntion to get the annot
retrive_annotation(effecotr_in_DE_exon, eff_name_annot)

effecotr_in_DEG = effector_set.intersection(reps_3)

print("\n%d effecotrs were found in the DE gene anlaysis" %
      (len(effecotr_in_DEG)))
# call a fucntion to get the annot
retrive_annotation(effecotr_in_DEG, eff_name_annot)


