# political-ads - WIP

# Political Advertising 

**Slack Channel**: #political-ads 

**Project Description**: Extracting and parsing data on political advertising from [FCC Public Files] (https://publicfiles.fcc.gov) and [related sources] (https://politicaladarchive.org/data/).

**Project Lead**: @pratheekrebala

## Project Goals

This project aims to develop a pipeline for fetching, cleaning and parsing the data on political ad spending available from the FCC's Public Files.

**Fetching**: Designing a pipeline to fetch data from the FCC API, this involves getting older data from the FCC's OPIF API and monitoring new filings using the RSS Feed.

**Archiving**: Some TV stations delete public files from the FCC system following the minimum retention period (~2yrs). A process for archiving these documents will allow for historical research.

**Pre-Processing**: All the files available on the Public File system are in PDF format. A significant number of these files are image based PDFs which need to be OCRd before they can be processed.

**Processing**: A processing pipeline to detect and extract relevant metadata from filings (e.g. Flight Dates, Invoice Amount, Number of Spots).

More TK.

## About Public Files

The Federal Communications Commission (FCC), per [47 CFR 73.3526] (https://www.law.cornell.edu/cfr/text/47/73.3526) requires that commercial television states keep a political file that documents the details the advertising activity of political candidates on their channel. The public files extensively detail the transactions that political campaigns and ad-buyers have with the TV station including price per spot, detailed schedules and program information. Some stations also choose to provide additional information about the targeted demographic and Cost Per-Engagement (CPE) information.

A few sample PDF files have been provided in the `samples` directory.

## Related Projects

[Sunlight AdSleuth] (https://github.com/sunlightlabs/fcc_political_ads)

[FCC Political Ads] (https://github.com/alexbyrnes/FCC-Political-Ads)
