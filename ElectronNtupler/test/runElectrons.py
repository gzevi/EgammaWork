import FWCore.ParameterSet.Config as cms

process = cms.Process("Ntupler")

process.load("FWCore.MessageService.MessageLogger_cfi")

#
# Define input data to read
#
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )

inputFilesAOD = cms.untracked.vstring(
    # AOD test files from /DYJetsToLL_M-50_13TeV-madgraph-pythia8/Phys14DR-PU20bx25_PHYS14_25_V1-v1/AODSIM
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/00CC714A-F86B-E411-B99A-0025904B5FB8.root',
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/040D9AF7-FB6B-E411-8106-0025907DBA06.root',
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/04442001-036C-E411-9C90-0025901D42C0.root',
    )    

inputFilesMiniAOD = cms.untracked.vstring(
    # MiniAOD test files from /DYJetsToLL_M-50_13TeV-madgraph-pythia8/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0432E62A-7A6C-E411-87BB-002590DB92A8.root',
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/06C61714-7E6C-E411-9205-002590DB92A8.root',
    '/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0EAD09A8-7C6C-E411-B903-0025901D493E.root'        ,
    )

#
# You can list here either AOD or miniAOD files, but not both types mixed
#
useAOD = False
if useAOD == True :
    inputFiles = inputFilesAOD
    print("AOD input files are used")
else :
    inputFiles = inputFilesMiniAOD
    print("MiniAOD input files are used")
process.source = cms.Source ("PoolSource", fileNames = inputFiles )                             

#
# Configure the ntupler module
#

process.ntupler = cms.EDAnalyzer('SimpleElectronNtupler',
                                 # The module automatically detects AOD vs miniAOD, so we configure both
                                 #
                                 # Common to all formats objects
                                 #
                                 pileup   = cms.InputTag("addPileupInfo"),
                                 rho      = cms.InputTag("fixedGridRhoFastjetAll"),
                                 beamSpot = cms.InputTag('offlineBeamSpot'),
                                 #
                                 # Objects specific to AOD format
                                 #
                                 electrons    = cms.InputTag("gedGsfElectrons"),
                                 genParticles = cms.InputTag("genParticles"),
                                 vertices     = cms.InputTag("offlinePrimaryVertices"),
                                 conversions  = cms.InputTag('conversions'),
                                 #
                                 # Objects specific to MiniAOD format
                                 #
                                 electronsMiniAOD    = cms.InputTag("slimmedElectrons"),
                                 genParticlesMiniAOD = cms.InputTag("prunedGenParticles"),
                                 verticesMiniAOD     = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                 conversionsMiniAOD  = cms.InputTag('reducedEgamma:reducedConversions'),
                                 )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('electron_ntuple.root')
                                   )


process.p = cms.Path(process.ntupler)
