import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part10of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part1of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part2of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part3of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part4of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part5of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part6of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part7of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part8of10_inMINIAODSIM.root',
       'file:////eos/uscms//store/user/sbein/Higgsino/step3_higgsino_susyall_mChipm105GeV_dm0p26GeV_pu_part9of10_inMINIAODSIM.root'
] )

'''
\scriptsize
\centering
\begin{columns}
\column{.4\textwidth}
\scriptsize
\item Baseline and SR of SUS-19-005 w. disappearing tracks
\item 
\begin{itemize}
\scriptsize
\item track selection
\begin{itemize}
\scriptsize
\item rectangular cuts on dxy, dz, isolation, etc.
\item short, medium and long tracks separated
\item PF candidate, lepton veto
\end{itemize}
\item event selection
\begin{itemize}
\scriptsize
\item n(jets)$\geq$2
\item $M_{T2}>200$ GeV
\item n(reco electron)=0
\item n(reco muon)=0
\item binning in $n_{\text{jets}}$, $H_{T}$
\end{itemize}
\end{itemize}
\column{.6\textwidth}
\centering
SUS-19-005 (c$\tau=$ 2 m)\\
\includegraphics[width=0.7\linewidth]{pdfs/4-MT2Limit}\\
\end{columns}
'''
