# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:54:10 2022

@author: andre
"""

import ROOT

#File locations and names ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

promt_filename_part_1 = "/eos/lhcb/user/a/alupato/B2Dpi_2016_90/D_prompt_track_2016_up_"
signal_filename = "/eos/lhcb/wg/b2oc/TD_Bs2Dsh_Run2/Data_FT_2017_v4_Run2_withMomentumScale/FINAL/B2DX_2016_Down_Bd2DPi_OFFLINE_KPiPi.root"
hist_promt_p1_M = ROOT.TH1D("hist_p1_M_promt", "", 50, 0, 600)
hist_promt_c2_M = ROOT.TH1D("hist_c2_M_promt", "", 50, 1700, 2000)
hist_promt_k3_M = ROOT.TH1D("hist_k3_M_promt", "", 50, 488, 500)
hist_promt_p4_M = ROOT.TH1D("hist_p4_M_promt", "", 50, 136, 142)
hist_promt_p5_M = ROOT.TH1D("hist_p5_M_promt", "", 50, 136, 142)
hist_promt_p1_M_cut = ROOT.TH1D("hist_p1_M_promt_cut", "", 50, 0, 600)
hist_promt_c2_M_cut = ROOT.TH1D("hist_c2_M_promt_cut", "", 50, 1700, 2000)
hist_promt_k3_M_cut = ROOT.TH1D("hist_k3_M_promt_cut", "", 50, 488, 500)
hist_promt_p4_M_cut = ROOT.TH1D("hist_p4_M_promt_cut", "", 50, 136, 142)
hist_promt_p5_M_cut = ROOT.TH1D("hist_p5_M_promt_cut", "", 50, 136, 142)

#Opening and reading in the data from the prompt files ~~~~~~~~~~~~~~~~~~~~~~~
for i in range(2, 10):
    
    promt_filename = promt_filename_part_1 + str(i) + ".root"
    inFile = ROOT.TFile.Open(promt_filename,"READ")
    promt_directory = inFile.Get("Bd2DPiOfflineTree")
    promt_tree = promt_directory.Get("DecayTree")
    

    for i in range(0, 20000):
        promt_tree.GetEntry(i)
        pion1_M = getattr(promt_tree, "lab1_M")
        charm2_M = getattr(promt_tree, "lab2_M")
        kaon3_M = getattr(promt_tree, "lab3_M")
        pion4_M = getattr(promt_tree, "lab4_M")
        pion5_M = getattr(promt_tree, "lab5_M")
        pion1_PIDe = getattr(promt_tree, "lab1_PIDe")
        pion5_PIDe = getattr(promt_tree, "lab5_PIDe")
        
        hist_promt_p1_M.Fill(pion1_M)
        hist_promt_c2_M.Fill(charm2_M)
        hist_promt_k3_M.Fill(kaon3_M)
        hist_promt_p4_M.Fill(pion4_M)
        hist_promt_p5_M.Fill(pion5_M)
        
        if(pion1_PIDe < 3 and pion5_PIDe < 3):
            hist_promt_p1_M_cut.Fill(pion1_M)
            hist_promt_c2_M_cut.Fill(charm2_M)
            hist_promt_k3_M_cut.Fill(kaon3_M)
            hist_promt_p4_M_cut.Fill(pion4_M)
            hist_promt_p5_M_cut.Fill(pion5_M)

print("prompt pion 1 cut efficiency promt:", 100*hist_promt_p1_M_cut.GetEntries()/hist_promt_p1_M.GetEntries(), "%")
print("prompt charm 2 cut efficiency sig:", 100*hist_promt_c2_M_cut.GetEntries()/hist_promt_c2_M.GetEntries(), "%")
print("prompt kaon 3 cut efficiency sig:", 100*hist_promt_k3_M_cut.GetEntries()/hist_promt_k3_M.GetEntries(), "%")
print("prompt pion 4 cut efficiency sig:", 100*hist_promt_p4_M_cut.GetEntries()/hist_promt_p4_M.GetEntries(), "%")
print("prompt pion 5 cut efficiency sig:", 100*hist_promt_p5_M_cut.GetEntries()/hist_promt_p5_M.GetEntries(), "%")

#Closing the prompt file and opening the signal file~~~~~~~~~~~~~~~~~~~~~~~~~~

inFile2 = ROOT.TFile.Open(signal_filename,"READ")
sig_tree = inFile2.Get("DecayTree")

hist_sig_p1_M = ROOT.TH1D("hist_p1_M_sig", "", 50, 0, 600)
hist_sig_c2_M = ROOT.TH1D("hist_c2_M_sig", "", 50, 1700, 2000)
hist_sig_k3_M = ROOT.TH1D("hist_k3_M_sig", "", 50, 488, 500)
hist_sig_p4_M = ROOT.TH1D("hist_p4_M_sig", "", 50, 136, 142)
hist_sig_p5_M = ROOT.TH1D("hist_p5_M_sig", "", 50, 136, 142)
hist_sig_p1_M_cut = ROOT.TH1D("hist_p1_M_sig_cut", "", 50, 0, 600)
hist_sig_c2_M_cut = ROOT.TH1D("hist_c2_M_sig_cut", "", 50, 1700, 2000)
hist_sig_k3_M_cut = ROOT.TH1D("hist_k3_M_sig_cut", "", 50, 488, 500)
hist_sig_p4_M_cut = ROOT.TH1D("hist_p4_M_sig_cut", "", 50, 136, 142)
hist_sig_p5_M_cut = ROOT.TH1D("hist_p5_M_sig_cut", "", 50, 136, 142)


for i in range(0, 20000):
    sig_tree.GetEntry(i)
    pion1_M = getattr(sig_tree, "lab1_M")
    charm2_M = getattr(sig_tree, "lab2_M")
    kaon3_M = getattr(sig_tree, "lab3_M")
    pion4_M = getattr(sig_tree, "lab4_M")
    pion5_M = getattr(sig_tree, "lab5_M")
    pion1_PIDe = getattr(sig_tree, "lab1_PIDe")
    pion5_PIDe = getattr(sig_tree, "lab5_PIDe")
    
    hist_sig_p1_M.Fill(pion1_M)
    hist_sig_c2_M.Fill(charm2_M)
    hist_sig_k3_M.Fill(kaon3_M)
    hist_sig_p4_M.Fill(pion4_M)
    hist_sig_p5_M.Fill(pion5_M)

    if(pion1_PIDe < 3 and pion5_PIDe < 3):
            hist_sig_p1_M_cut.Fill(pion1_M)
            hist_sig_c2_M_cut.Fill(charm2_M)
            hist_sig_k3_M_cut.Fill(kaon3_M)
            hist_sig_p4_M_cut.Fill(pion4_M)
            hist_sig_p5_M_cut.Fill(pion5_M)
            
print("signal pion 1 cut efficiency sig:", 100*hist_sig_p1_M_cut.GetEntries()/hist_sig_p1_M.GetEntries(), "%")
print("signal charm 2 cut efficiency sig:", 100*hist_sig_c2_M_cut.GetEntries()/hist_sig_c2_M.GetEntries(), "%")
print("signal kaon 3 cut efficiency sig:", 100*hist_sig_k3_M_cut.GetEntries()/hist_sig_k3_M.GetEntries(), "%")
print("signal pion 4 cut efficiency sig:", 100*hist_sig_p4_M_cut.GetEntries()/hist_sig_p4_M.GetEntries(), "%")
print("signal pion 5 cut efficiency sig:", 100*hist_sig_p5_M_cut.GetEntries()/hist_sig_p5_M.GetEntries(), "%")

#Creating a file for the canvases ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

output_hist_file = ROOT.TFile.Open("comparing_sig_propmt_mass.root", "RECREATE")
output_hist_file.cd()

#doing fit stuff ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dmass = ROOT.RooRealVar("dmass", "dmass", 1700, 2000)
fithist = ROOT.RooDataHist("fithist", "fithist", [dmass], hist_promt_c2_M)
frame = dmass.frame(Title="histogram c2 mass")
fithist.plotOn(frame)
mean = ROOT.RooRealVar("mean", "mean",1860, 1700, 2000)
sigma = ROOT.RooRealVar("sigma", "sigma", 30, 0.1, 50)
gauss = ROOT.RooGaussian("gauss", "gauss", dmass, mean, sigma)
gauss.fitTo(fithist)
gauss.plotOn(frame)
frame.GetYaxis().SetTitle( "Counts" )
frame.GetXaxis().SetTitle( "m(D) [MeV/c^{2}]" )
c = ROOT.TCanvas("fitcanvas", "fitcanvas", 900, 1800)
c.Divide(1, 3)
c.cd(1)
frame.GetYaxis().SetTitleOffset(1.6)
frame.Draw()

residhist = ROOT.RooHist(frame.residHist())
pullhist = ROOT.RooHist(frame.pullHist())
frame2 = dmass.frame(Title="histogram c2 mass resid")
frame2.addPlotable(residhist, "p")
frame3 = dmass.frame(Title="histogram c2 mass pull")
frame3.addPlotable(pullhist, "p")
c.cd(2)
#(c.GetSelectedPad()).SetPad(0.0, 0.0, 300.0, 400.0)
frame2.GetYaxis().SetTitleOffset(1.6)
frame2.Draw()
c.cd(3)
frame3.GetYaxis().SetTitleOffset(1.6)
frame3.Draw()

c.Print("attempting_fit.pdf")

canvas = ROOT.TCanvas("canvas","", 1400, 1000)


#Histogram lab1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p1_M.Scale(hist_sig_p1_M.Integral()/hist_promt_p1_M.Integral(), "nosw2")
hist_promt_p1_M.GetXaxis().SetTitle("m_{ ll } [ MeV/c^{2} ] " )
hist_promt_p1_M.GetYaxis().SetTitle( "Counts" )
# hist_promt_p1_M.SetStats(0)
hist_promt_p1_M.Draw()
hist_sig_p1_M.SetLineColor(ROOT.kRed)
hist_sig_p1_M.Draw("same")
leg = ROOT.TLegend(.50,.70,.68,.85)
leg.AddEntry(hist_sig_p1_M,"B2DPi_sig","f")
leg.AddEntry(hist_promt_p1_M,"B2DPi_promt","f")
leg.Draw()
canvas.Print("Histogram_pion_lab1.pdf")
canvas.Clear()

#Histogram lab2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_c2_M.Scale(hist_sig_c2_M.Integral()/hist_promt_c2_M.Integral(), "nosw2")
hist_sig_c2_M.GetXaxis().SetTitle( " m(D^{+}) [ MeV/c^{2} ] " )
hist_sig_c2_M.GetYaxis().SetTitle( "Counts" )
# hist_sig_c2_M.SetStats(0)
# hist_promt_c2_M.SetStats(0)
hist_sig_c2_M.SetLineColor(ROOT.kRed)
hist_sig_c2_M.Draw()
hist_promt_c2_M.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_sig_c2_M,"B2DPi_sig","f")
leg.AddEntry(hist_promt_c2_M,"B2DPi_promt","f")
leg.Draw()
canvas.Print("Histogram_charm_lab2.pdf")
canvas.Clear()

#Histogram lab3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_k3_M.Scale(hist_sig_k3_M.Integral()/hist_promt_k3_M.Integral(), "nosw2")
hist_promt_k3_M.GetXaxis().SetTitle( " m(K) [ MeV/c^{2} ] " )
hist_promt_k3_M.GetYaxis().SetTitle( "Counts" )
hist_promt_k3_M.SetStats(0)
hist_promt_k3_M.Draw()
hist_sig_k3_M.SetLineColor(ROOT.kRed)
hist_sig_k3_M.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_sig_k3_M,"B2DPi_sig","f")
leg.AddEntry(hist_promt_k3_M,"B2DPi_promt","f")
leg.Draw()
canvas.Print("Histogram_kaon_lab3.pdf")
canvas.Clear()

#Histogram lab4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p4_M.Scale(hist_sig_p4_M.Integral()/hist_promt_p4_M.Integral(), "nosw2")
hist_promt_p4_M.GetXaxis().SetTitle( " m(\pi) [ MeV/c^{2} ] " )
hist_promt_p4_M.GetYaxis().SetTitle( "Counts" )
hist_promt_p4_M.SetStats(0)
hist_promt_p4_M.Draw()
hist_sig_p4_M.SetLineColor(ROOT.kRed)
hist_sig_p4_M.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_sig_p4_M,"B2DPi_sig","f")
leg.AddEntry(hist_promt_p4_M,"B2DPi_promt","f")
leg.Draw()
canvas.Print("Histogram_pion_lab4.pdf")
canvas.Clear()

#Histogram lab5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p5_M.Scale(hist_sig_p5_M.Integral()/hist_promt_p5_M.Integral(), "nosw2")
hist_promt_p5_M.GetXaxis().SetTitle( " m(\pi) [ MeV/c^{2} ] " )
hist_promt_p5_M.GetYaxis().SetTitle( "Counts" )
hist_promt_p5_M.SetStats(0)
hist_promt_p5_M.Draw()
hist_sig_p5_M.SetLineColor(ROOT.kRed)
hist_sig_p5_M.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_sig_p5_M,"B2DPi_sig","f")
leg.AddEntry(hist_promt_p5_M,"B2DPi_promt","f")
leg.Draw()
canvas.Print("Histogram_pion_lab5.pdf")
canvas.Clear()

#Histogram cut lab1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p1_M_cut.Scale(hist_sig_p1_M_cut.Integral()/hist_promt_p1_M_cut.Integral(), "nosw2")
hist_promt_p1_M_cut.GetXaxis().SetTitle("m_{ ll } [ MeV/c^{2} ] " )
hist_promt_p1_M_cut.GetYaxis().SetTitle( "Counts" )
hist_promt_p1_M_cut.SetStats(0)
hist_promt_p1_M_cut.Draw()
hist_sig_p1_M_cut.SetLineColor(ROOT.kRed)
hist_sig_p1_M_cut.Draw("same")
leg = ROOT.TLegend(.50,.70,.68,.85)
leg.AddEntry(hist_promt_p1_M_cut,"B2DPi_promt_cut","f")
leg.AddEntry(hist_sig_p1_M_cut,"B2DPi_sig_cut","f")
leg.Draw()
canvas.Print("Histogram_cut_pion_lab1.pdf")
canvas.Clear()

#Histogram cut lab2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_c2_M_cut.Scale(hist_sig_c2_M_cut.Integral()/hist_promt_c2_M_cut.Integral(), "nosw2")
hist_sig_c2_M_cut.GetXaxis().SetTitle( " m(D^{+}) [ MeV/c^{2} ] " )
hist_sig_c2_M_cut.GetYaxis().SetTitle( "Counts" )
hist_sig_c2_M_cut.SetStats(0)
hist_promt_c2_M_cut.SetStats(0)
hist_sig_c2_M_cut.SetLineColor(ROOT.kRed)
hist_sig_c2_M_cut.Draw()
hist_promt_c2_M_cut.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_promt_c2_M_cut,"B2DPi_promt_cut","f")
leg.AddEntry(hist_sig_c2_M_cut,"B2DPi_sig_cut","f")
leg.Draw()
canvas.Print("Histogram_cut_charm_lab2.pdf")
canvas.Clear()

#Histogram cut lab3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_k3_M_cut.Scale(hist_sig_k3_M_cut.Integral()/hist_promt_k3_M_cut.Integral(), "nosw2")
hist_promt_k3_M_cut.GetXaxis().SetTitle( " m(K) [ MeV/c^{2} ] " )
hist_promt_k3_M_cut.GetYaxis().SetTitle( "Counts" )
hist_promt_k3_M_cut.SetStats(0)
hist_promt_k3_M_cut.Draw()
hist_sig_k3_M_cut.SetLineColor(ROOT.kRed)
hist_sig_k3_M_cut.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_promt_k3_M_cut,"B2DPi_promt_cut","f")
leg.AddEntry(hist_sig_k3_M_cut,"B2DPi_sig_cut","f")
leg.Draw()
canvas.Print("Histogram_cut_kaon_lab3.pdf")
canvas.Clear()

#Histogram cut lab4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p4_M_cut.Scale(hist_sig_p4_M_cut.Integral()/hist_promt_p4_M_cut.Integral(), "nosw2")
hist_promt_p4_M_cut.GetXaxis().SetTitle( " m(\pi) [ MeV/c^{2} ] " )
hist_promt_p4_M_cut.GetYaxis().SetTitle( "Counts" )
hist_promt_p4_M_cut.SetStats(0)
hist_promt_p4_M_cut.Draw()
hist_sig_p4_M_cut.SetLineColor(ROOT.kRed)
hist_sig_p4_M_cut.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_promt_p4_M_cut,"B2DPi_promt_cut","f")
leg.AddEntry(hist_sig_p4_M_cut,"B2DPi_sig_cut","f")
leg.Draw()
canvas.Print("Histogram_cut_pion_lab4.pdf")
canvas.Clear()

#Histogram cut lab5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

hist_promt_p5_M_cut.Scale(hist_sig_p5_M_cut.Integral()/hist_promt_p5_M_cut.Integral(), "nosw2")
hist_promt_p5_M_cut.GetXaxis().SetTitle( " m(\pi) [ MeV/c^{2} ] " )
hist_promt_p5_M_cut.GetYaxis().SetTitle( "Counts" )
hist_promt_p5_M_cut.SetStats(0)
hist_promt_p5_M_cut.Draw()
hist_sig_p5_M_cut.SetLineColor(ROOT.kRed)
hist_sig_p5_M_cut.Draw("same")
leg = ROOT.TLegend(.70,.70,.88,.85)
leg.AddEntry(hist_promt_p5_M_cut,"B2DPi_promt_cut","f")
leg.AddEntry(hist_sig_p5_M_cut,"B2DPi_sig_cut","f")
leg.Draw()
canvas.Print("Histogram_cut_pion_lab5.pdf")
canvas.Clear()
#Histogram styling ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#leg.SetBorderSize(0) # no border
#leg.SetFillColor(0) # probably kWhite
#leg.SetFillStyle(0) # I'm guessing this just means pure color, no patterns 
#leg.SetTextFont(42)
#leg.SetTextSize(0.035) # somewhat large, may need to play with this to make the plot look ok
#leg = ROOT.TLegend(.70,.70,.80,.85) # TLegend(x1,y1,x2,y2) where x,y are in units of percentage of canvas (i.e. x,y \in [0,1])
#leg.AddEntry(hist_promt_c2_M,"B2DPi_promt","f") # AddEntry(TGraph/TH1D varName, what you want the legend to say for this graph, show the line)
 hello friend plz work
    
    