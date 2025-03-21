from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
	columns={
		"bs-sample_name": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=True,
			coerce=False,
			required=True,
			description="Identifier name used for BioSample. Max length is 50 characters.",
			title="sample_name",
		),
		"bs-sample_title": Column(
			dtype="object",
			checks=[
				Check.str_matches(r"^(?!\s*$).+"),
			],
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Descriptive title for sample.",
			title="sample title",
		),
		"bs-sample_description": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Optional description for sample.",
			title="sample description",
		),
		"bs-isolate": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Organism\". identification or description of the specific individual from which this sample was obtained",
			title="isolate",
		),
		"bs-cultivar": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Organism\". cultivar name - cultivated variety of plant",
			title="cultivar",
		),
		"bs-ecotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Organism\". a population within a given species displaying genetically based, phenotypic traits that reflect adaptation to a local habitat, e.g., Columbia",
			title="ecotype",
		),
		"bs-age": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Age/stage\". age at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees",
			title="age",
		),
		"bs-dev_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=True,
			description="At least one required: Group \"Age/stage\". Developmental stage at the time of sampling.",
			title="development stage",
		),
		"bs-geo_loc_name": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Geographical origin of the sample; use the appropriate name from this list http://www.insdc.org/documents/country-qualifier-vocabulary. Use a colon to separate the country or ocean from more detailed information about the location, eg \"Canada: Vancouver\" or \"Germany: halfway down Zugspitze, Alps\"",
			title="geographic location",
		),
		"bs-tissue": Column(
			dtype="object",
			checks=None,
			nullable=False,
			unique=False,
			coerce=False,
			required=True,
			description="Type of tissue the sample was taken from.",
			title="tissue",
		),
		"bs-biomaterial_provider": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="name and address of the lab or PI, or a culture collection identifier",
			title="biomaterial provider",
		),
		"bs-cell_line": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of the cell line.",
			title="cell line",
		),
		"bs-cell_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Type of cell of the sample or from which the sample was obtained.",
			title="cell type",
		),
		"bs-collected_by": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of persons or institute who collected the sample",
			title="collected by",
		),
		"bs-culture_collection": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Name of source institute and unique culture identifier. See the description for the proper format and list of allowed institutes, http://www.insdc.org/controlled-vocabulary-culturecollection-qualifier",
			title="culture collection",
		),
		"bs-disease": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="list of diseases diagnosed; can include multiple diagnoses. the value of the field depends on host; for humans the terms should be chosen from DO (Disease Ontology), free text for non-human. For DO terms, please see http://gemina.svn.sourceforge.net/viewvc/gemina/trunk/Gemina/ontologies/gemina_symptom.obo?view=log",
			title="disease",
		),
		"bs-disease_stage": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="stage of disease at the time of sampling.",
			title="disease stage",
		),
		"bs-genotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="observed genotype",
			title="genotype",
		),
		"bs-growth_protocol": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="growth protocol",
		),
		"bs-height_or_length": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="measurement of height or length",
			title="height or length",
		),
		"bs-isolation_source": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived.",
			title="isolation source",
		),
		"bs-lat_lon": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="The geographical coordinates of the location where the sample was collected. Specify as degrees latitude and longitude in format \"d[d.dddd] N|S d[dd.dddd] W|E\", eg, 38.98 N 77.11 W",
			title="latitude and longitude",
		),
		"bs-phenotype": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Phenotype of sampled organism. For Phenotypic quality Ontology (PATO) (v1.269) terms, please see http://bioportal.bioontology.org/visualize/44601",
			title="phenotype",
		),
		"bs-population": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="for human: ; for plants: filial generation, number of progeny, genetic structure",
			title="population",
		),
		"bs-sample_type": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Sample type, such as cell culture, mixed culture, tissue sample, whole organism, single cell, metagenomic assembly",
			title="sample type",
		),
		"bs-sex": Column(
			dtype="object",
			checks=Check.str_matches(r"(?i)(\W|^)(male|female|pooled male and female|neuter|hermaphrodite|intersex|not determined|missing|not applicable|not collected|not provided|restricted access)(\W|$)"),
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="physical sex of sampled organism",
			title="sex",
		),
		"bs-specimen_voucher": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Identifier for the physical specimen. Use format: \"[<institution-code>:[<collection-code>:]]<specimen_id>\", eg, \"UAM:Mamm:52179\". Intended as a reference to the physical specimen that remains after it was analyzed. If the specimen was destroyed in the process of analysis, electronic images (e-vouchers) are an adequate substitute for a physical voucher specimen. Ideally the specimens will be deposited in a curated museum, herbarium, or frozen tissue collection, but often they will remain in a personal or laboratory collection for some time before they are deposited in a curated collection. There are three forms of specimen_voucher qualifiers. If the text of the qualifier includes one or more colons it is a 'structured voucher'. Structured vouchers include institution-codes (and optional collection-codes) taken from a controlled vocabulary maintained by the INSDC that denotes the museum or herbarium collection where the specimen resides, please visit: http://www.insdc.org/controlled-vocabulary-specimenvoucher-qualifier.",
			title="specimen voucher",
		),
		"bs-temp": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="temperature of the sample at time of sampling",
			title="temperature",
		),
		"bs-treatment": Column(
			dtype="object",
			checks=None,
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			title="treatment",
		),
		"bs-title": Column(
			dtype="object",
			checks=[
				Check(lambda s: s.nunique() == 1),
			],
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Optional internal field for how the BioSample submission should be named when viewed from the NCBI submission portal. If not provided, when performing submissions <--submission_name> with the suffix \"-BS\" will be used instead.",
			title="biosample submission portal name",
		),
		"bs-comment": Column(
			dtype="object",
			checks=[
				Check(lambda s: s.nunique() == 1),
			],
			nullable=True,
			unique=False,
			coerce=False,
			required=False,
			description="Optional internal field explaining the purpose of the submission for when interacting and resolving submission issues with NCBI.",
			title="biosample submission portal description",
		)
	},
	checks=[
		Check(lambda df: ~(df["bs-isolate"].isnull() & df["bs-cultivar"].isnull() & df["bs-ecotype"].isnull()), ignore_na = False),
		Check(lambda df: ~(df["bs-age"].isnull() & df["bs-dev_stage"].isnull()), ignore_na = False),
	],
	index=None,
	coerce=False,
	strict="filter",
	name="biosample_package_Plant.1.0_schema",
	ordered=False,
	unique=None,
	report_duplicates="all",
	unique_column_names=True,
	add_missing_columns=False,
	title="BioSample package Plant.1.0 schema",
	description="Schema validation for BioSample database using Plant.1.0 package.",
)