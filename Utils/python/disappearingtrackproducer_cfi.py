import FWCore.ParameterSet.Config as cms

disappearingTracks = cms.EDProducer("DisappearingTrackProducer",
                                    selectedTracks = cms.InputTag("generalTracks"),
                                    selectedElectrons = cms.InputTag("gedGsfElectrons"),
                                    selectedMuons = cms.InputTag("muons"),
                                    selectedPFJets = cms.InputTag("ak4PFJetsCHS"),
                                    selectedPFCand = cms.InputTag("particleFlow"),
                                    minTrackPt = cms.double(15),
                                    maxTrackEta = cms.double(2.4),
                                    coneRelIsoDR = cms.double(0.3),
                                    conePtSumMaxPtPercentage = cms.double(0.05),
                                    minTrackJetDR = cms.double(0.5),
                                    minTrackLeptonDR = cms.double(0.15),
                                    RequireNumberOfValidPixelHits = cms.int32(1),
                                    RequireNumberOfValidTrackerHits = cms.int32(7),
                                    maxDxy = cms.double(0.02),
                                    maxDz = cms.double(0.5),
                                    selectedEcalRecHitsEB = cms.InputTag("reducedEcalRecHitsEB"),
                                    selectedEcalRecHitsEE = cms.InputTag("reducedEcalRecHitsEE"),
                                    selectedEcalRecHitsES = cms.InputTag("reducedEcalRecHitsES"),
                                    selectedHcalRecHits = cms.InputTag("reducedHcalRecHits"),
                                    selectedCaloJets = cms.InputTag("ak4CaloJets"),
                                    useCaloJetsInsteadOfHits = cms.bool(False),
                                    minMissingOuterHits = cms.int32(3),
                                    caloEnergyDepositionMaxDR = cms.double(0.5),
                                    caloEnergyDepositionMaxE = cms.double(10),
                                    deadNoisyDR = cms.double(0.05),
                                    dEdxEstimator = cms.string('dedxHarmonic2'),
                                    doDeDx = cms.bool(True),
                                    PrimaryVertex = cms.InputTag('offlinePrimaryVertices'),
                                    maxChargedPFCandSumDR = cms.double(0.01),
                                    maxNeutralPFCandSumDR = cms.double(0.05),
                                    )
