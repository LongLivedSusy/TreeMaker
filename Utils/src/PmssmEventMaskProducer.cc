// -*- C++ -*-
// Package:    TreeMaker
// Class:      PmssmEventMaskProducer
// Authors:   Sam Bein 
//         Created:  Wed March 7, 2014
//         Modified: Thurs March 3, 2021

#include <memory>
#include <iostream>
#include <unordered_set>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include <DataFormats/HepMCCandidate/interface/GenParticle.h>

#include <vector>

class PmssmEventMaskProducer : public edm::global::EDProducer<> {

public:
    explicit PmssmEventMaskProducer(const edm::ParameterSet&);
    ~PmssmEventMaskProducer() override;

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
    void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

    // ----------member data ---------------------------

    edm::InputTag genCollection;
    edm::EDGetTokenT<edm::View<reco::GenParticle>> genCollectionTok;

};


PmssmEventMaskProducer::PmssmEventMaskProducer(const edm::ParameterSet& iConfig):
  genCollection(iConfig.getParameter<edm::InputTag>("genCollection")),
  genCollectionTok(consumes<edm::View<reco::GenParticle>>(genCollection))
{
    produces< bool >("EventMask");
    produces< bool >("EventMaskRoyal");    
}

PmssmEventMaskProducer::~PmssmEventMaskProducer() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
}


// ------------ method called for each event  ------------
void PmssmEventMaskProducer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
    using namespace edm;

    bool EventMask = true;
   
    
    edm::Handle< View<reco::GenParticle> > genPartCands;
    iEvent.getByToken(genCollectionTok, genPartCands);

    //Determine highest pT of a SM particle that crosses the beam pipe radius
    double ptmax = -1.0;   
    for(const auto& iPart : *genPartCands) {
        if (iPart.numberOfDaughters()>0)
        {
	  if(!(iPart.pt()>10.)) continue;
	  const reco::Candidate * daughter1 = iPart.daughter(0);
	  float origin_xy_cm = std::sqrt(iPart.vx()*iPart.vx() + iPart.vy()*iPart.vy());
	  float endpoint_xy_cm = std::sqrt(daughter1->vx()*daughter1->vx()+daughter1->vy()*daughter1->vy());
	  if (origin_xy_cm < 4 && endpoint_xy_cm > 4.3 && abs(iPart.pdgId())<1000000)
	    ptmax = std::max(ptmax, iPart.pt());
	}
    }

    if (ptmax>10) EventMask = true;
    else EventMask = false;

    bool EventMaskRoyal = true;
    //Determine highest pT of a SM particle that crosses the beam pipe radius
    ptmax = -1.0;   
    for(const auto& iPart : *genPartCands) {
        if (iPart.numberOfDaughters()>0)
        {
	  const reco::Candidate * daughter1 = iPart.daughter(0);
	  if(!(iPart.pt()>10)) continue;
	  float origin_xy_cm = std::sqrt(iPart.vx()*iPart.vx() + iPart.vy()*iPart.vy());
	  float endpoint_xy_cm = std::sqrt(daughter1->vx()*daughter1->vx()+daughter1->vy()*daughter1->vy());
	  if (!(origin_xy_cm < 4 && endpoint_xy_cm > 4.3 && abs(iPart.pdgId())<1000000)) continue;
	  if (iPart.pt()>ptmax) continue;
	  const reco::Candidate * dynamicMother;
	  dynamicMother = iPart.mother(0);
	  while (dynamicMother){
	    if (abs(dynamicMother->pdgId())>1000000 && abs(dynamicMother->pdgId())<3000000)
	      {
		ptmax = std::max(ptmax, iPart.pt());
		std::cout << "it's happening!" << std::endl;
	      }
	    dynamicMother = dynamicMother->mother(0);
	  }	         
	}
    }
    
    if (ptmax>10.) EventMaskRoyal = true;
    else EventMaskRoyal = false;

    auto EventMaskRoyal_bool = std::make_unique<bool>(EventMaskRoyal);
    iEvent.put(std::move(EventMaskRoyal_bool), "EventMaskRoyal");
    
    auto EventMask_bool = std::make_unique<bool>(EventMask);
    iEvent.put(std::move(EventMask_bool), "EventMask");
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PmssmEventMaskProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
}

#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(PmssmEventMaskProducer);
