# In-Class Activity: Ethical Audit of Your AI Solution

## Learning Outcome Covered

**4.1** Analyze AI solutions from multiple lenses: accessibility, ethics, equity, privacy, security, sustainability, and well-being.

## Activity Overview

Evaluate the CanopyIQ Tree Canopy Decision Support System (DSS) as a commercial product being sold to a municipal client. The audit is written from the position of a vendor preparing for a City of Kitchener procurement, so each lens is assessed as a business risk to the client and a commercial risk to us, not only as a technical property of the model.

---

## Step 1: Project Reframing

### What problem does the AI solve — and what is the client buying?

CanopyIQ integrates municipal tree records, LiDAR canopy data, and Landsat temperature data to prioritize budget allocation across 52 planning communities and to estimate tree removal probability. The City of Kitchener is not buying a model; it is buying **budget defensibility** — the ability to show council and residents that forestry spending follows a documented, repeatable method rather than reactive storm response, which currently triggers 50–100% emergency surcharges.

- **Commercial model:** SaaS licence sold to the City of Kitchener, with implementation and annual support. Kitchener is the beachhead client; Waterloo and Cambridge are the expansion path.
- **Value proposition:** approximately $115,000 CAD in annual avoided cost, which is also our pricing anchor and the number the contract will be judged against at renewal.

### Who are the decision-makers and affected parties?

| Stakeholder | Role in the deal |
|---|---|
| Director of Operations / Forestry | Product champion; owns the operational pain |
| Procurement & Legal Services | Runs the RFP, sets contract and liability terms |
| City Clerk / Privacy Office | MFIPPA compliance and Privacy Impact Assessment sign-off |
| Corporate IT & Security | Security review, Cityworks integration approval |
| City Council | Approves the budget line; asks why one ward ranks below another |
| Field crews (unionized) | Daily users; adoption determines renewal |
| Residents | Experience the outcome; source of complaints and FOI requests |

### What decisions does the AI influence?

- Which planning communities are prioritized for pruning, planting, and inspection.
- Which individual trees are flagged with elevated removal probability.
- How the municipal tree management budget is distributed across wards.

---

## Step 2: Ethical Audit

Each lens is assessed for **business impact on the City** and **commercial exposure for us as the vendor**.

| Lens | Key Questions | Business Analysis | Risk Level |
|---|---|---|---|
| **Accessibility** | Can people with diverse abilities use it? | **City:** Kitchener is a designated public sector organization under Ontario's IASR (O. Reg. 191/11). Section 14 requires public-facing web content to meet WCAG 2.0 Level AA, and Section 5 requires accessibility criteria to be applied *when procuring* goods and services. A map-only dashboard with colour-coded priority tiers cannot be published by the City without exposing it to a compliance complaint. **Us:** this is a procurement disqualifier, not a nice-to-have — a non-conformant demo can remove us from the shortlist before price is ever discussed. | **High** |
| **Ethics** | Is the decision-making transparent and defensible? | **City:** once the City holds a documented removal-probability score for a specific tree, that record is discoverable. If a flagged tree later fails and causes injury or property damage, opposing counsel will ask why the City had notice and did not act. The scoring system converts an unknown risk into a documented one. **Us:** the classifier leans heavily on the *Fraxinus* / EAB signature, so any marketing language implying general mortality prediction becomes a misrepresentation exposure under the contract. | **High** |
| **Equity** | Does it bias budget outcomes across wards? | **City:** the 0.25 weights are effectively a budget allocation policy. A ward councillor whose community ranks low will challenge the method in a public meeting, and staff must be able to defend it in three minutes. **Us:** if weights are seen as a consultant's choice rather than a council decision, the tool becomes politically toxic and the renewal fails. | **Medium** |
| **Privacy** | Is data collected, stored, or misused? | **City:** as an institution under MFIPPA, Kitchener must respond to a resident requesting the risk score attached to the tree in front of their home. What is releasable must be decided before launch, not at the first request. A Privacy Impact Assessment will be a condition of sign-off. **Us:** hosting municipal records makes us a service provider under the City's records custody obligations, including Canadian data residency expectations. | **Medium** |
| **Security** | Can the system be attacked or manipulated? | **City:** the DSS writes maintenance schedules into Cityworks, so a compromise moves real work orders and real budget. Ontario municipalities are recurring ransomware targets, and this integration will attract scrutiny from Corporate IT. **Us:** we must pass a municipal security review and carry cyber liability coverage; failure here stalls the deal indefinitely at the IT gate. | **High** |
| **Sustainability** | Does it consume excessive resources? | **City:** the tool must demonstrably support Kitchener's corporate canopy and climate targets, because that is what justifies the budget line to council. A removal-heavy recommendation set that reduces net canopy would undermine the very target it was purchased to advance. **Us:** batch seasonal processing keeps hosting cost low and margin predictable. | **Low** |
| **Well-being** | Does it affect the people who use it? | **City:** field crews are unionized, and changing how daily work is assigned may require consultation under the collective agreement. Publicly labelling a community "low priority" generates councillor calls and reputational damage. **Us:** low crew adoption is the single most common cause of municipal software non-renewal — if crews do not use it, the savings never materialize and the contract dies at year two. | **Medium** |

> Regulatory items above reflect general Ontario requirements and should be confirmed with the City Clerk and Legal Services during procurement.

---

## Step 3: Red Flag Identification

- **1 Critical Risk — Liability transfer through documented notice.** Selling a system that generates and stores per-tree removal probabilities shifts the City from "we did not know" to "we had a score and did not act." Without contractual and procedural framing, we are selling our client a litigation exposure alongside a savings tool.
- **1 Moderate Risk — Accessibility as a procurement gate.** Under IASR Section 5, Kitchener must apply accessibility criteria when acquiring software. A map-first interface with no accessible equivalent is not a usability defect; it is a bid-eliminating defect.
- **1 Responsible Design Choice — "System advises, human decides."** The Green Equity KPI (at least 40% of the proactive budget to census tracts in the bottom 30% of income) gives council a defensible fairness commitment, and mandatory certified arborist inspection keeps decision authority — and therefore legal accountability — with the City's qualified staff.

---

## Step 4: Ethical Redesign

### Product controls

- **Data-coverage confidence flag** so under-inventoried communities are routed to fieldwork rather than scored as low priority, protecting the City from an equity challenge at council.
- **Tract-level joins enforced in the data model**, prohibiting any link between census income and individual tree coordinates, so the City's MFIPPA position is structural rather than procedural.
- **WCAG 2.1 AA tabular view** of the ranked communities (already exported as `canopyiq_index.csv`), exceeding the WCAG 2.0 AA legal floor and usable as a differentiator in the bid response.
- **Model card and explainability layer** documenting the *Fraxinus* dependency and feature importance, so the City's own disclosure obligations are satisfied by material we supply.
- **Immutable override audit log** giving the City an evidentiary record of who changed what and why.
- **Replanting work-order pairing** so every removal recommendation carries a planting recommendation, keeping the tool aligned with the City's canopy target.

### Commercial and contractual controls

- **Advisory-only clause** in the master service agreement stating that outputs are planning inputs and that no removal or safety decision is authorized by the software alone.
- **Agreed savings baseline** signed off with Forestry before go-live, so the $115,000 figure is measured against a number both parties accepted rather than disputed at renewal.
- **Weight-setting workshop with council staff** so the 0.25 weights become a client decision on record. The Monte Carlo results (median Spearman ρ = 0.996 across 1,000 runs, top-15 communities preserved) let us show that reasonable weight changes do not destabilize the plan.
- **Data ownership and exit terms**: the City owns its data and receives a full export on termination, which removes the lock-in objection that municipal procurement routinely raises.
- **Data-sharing agreement as a prerequisite for expansion.** Kitchener, Waterloo, and Cambridge are separate legal entities. The cross-city performance advantage we observed (Kitchener-trained model transferring at ROC-AUC 0.758) is only realizable if an inter-municipal data-sharing agreement exists. This is a contractual dependency in the expansion plan, not a technical one.

---

## Step 5: Final Verdict

**Deploy with Conditions**

**Justification:** The business case is sound — roughly $115,000 CAD in annual avoided cost against reactive storm surcharges — but the product cannot be sold as an autonomous decision system. Deployment proceeds on five conditions: all removal actions are deferred to certified arborist inspection; the model card and its *Fraxinus* limitation are published to the client; the Green Equity KPI is contractually reported each fiscal year; an accessible tabular export ships in version one; and a Privacy Impact Assessment is completed with the City Clerk before launch. Kitchener is delivered first, with expansion to Waterloo and Cambridge gated on a signed inter-municipal data-sharing agreement.

---

## Step 6: Peer Critique Reflection

> **"Would I trust this system if I were the client?"**

As Director of Operations, yes — with conditions. The index is transparent enough to defend at a council meeting, the equity commitment is measurable, and the override function means the tool supports professional judgment rather than displacing it. What would make the City hesitate is not model accuracy but the liability question: the moment forestry holds a documented risk score, the standard of care changes. That has to be addressed in the contract and in the City's own operating procedure, not in the software.

> **"Would you take legal responsibility for this AI system?"**

Not for field outcomes, and the contract must say so plainly. We accept responsibility for what a vendor can control: accuracy of the documented method, disclosed model limitations, accessibility conformance, security of the hosted environment, and availability under the SLA. We do not accept responsibility for tree failures or removal decisions, because those require certified arborist judgment that the City employs and we do not. This allocation is only defensible because the product is genuinely advisory — if we ever automated the removal decision, we would be accepting that liability whether the contract acknowledged it or not.
