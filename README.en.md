<!-- ⚠️ EN-TETE : identique au README francais. Le logo est FLOTTE, le titre est en ###
     (h1 et h2 portent une bordure que GitHub dessine sur toute la largeur et qui traverserait
     le logo), et la ligne est DESSINEE EN TEXTE parce qu un <hr> est un bloc et retraverserait
     le logo lui aussi. Longueur FIXE : plus longue, elle se replie sur deux rangees. -->
![le-cabinet — French law, tax, business and personal finance](assets/banner.jpg)

🇫🇷 [Français](README.md) · 🇬🇧 **English**

### <img src="assets/logo.png" align="left" width="124" alt=""> le-cabinet

────────────────────────────────────────────────────────<br>
**Nine roles for AI agents, covering French law, tax, business finance and personal finance.**<br>
For your business *and* your private life.

<br clear="left">

[![gate](https://github.com/Sjrazaviebra/le-cabinet/actions/workflows/gate.yml/badge.svg)](https://github.com/Sjrazaviebra/le-cabinet/actions/workflows/gate.yml)

> ⚠️ **The reference files are written in French, and that is deliberate** — French law is written
> in French, and so are the forms, the counters and the letters you will receive. **But every role
> answers in your language**, and keeps the French term with a short gloss: *« a récépissé (the
> receipt proving your application is being processed) »*. That word is the one you will have to say
> at the counter and recognise on a letter.

---

## ⭐ Who this is really for

**People who live in France and do not read French.** Not people curious about French law from abroad.

If you are an expat, a foreign student, a newly arrived employee, a founder, or a spouse — the rules
that decide your housing, your job, your residence permit and your taxes are written in a language
you are still learning, and the stakes are real: a missed deadline can close a right permanently.

★ This is stated inside the roles themselves. The `immigration` role says it plainly: **the people
who need this most rarely speak French, and almost never know the French terms for what they need.**

⚠️ **None of this content applies outside France.** Micro-entreprise, TVA, URSSAF, prud'hommes,
surendettement, titre de séjour — these are French devices, not general finance. A role will tell you
so rather than improvise an answer for another country.

## The nine roles

| Role | Call | Covers |
|---|---|---|
| **Comptable** | `/comptable` | Your business: legal form, micro-entreprise, VAT, bookkeeping, year-end, invoicing, payroll, unemployment and company creation. |
| **Impôts** | `/impots` | Your household: income tax return, brackets, tax household, investments and crypto, property, wealth tax, claims and audits. |
| **Financement** | `/financement` | Your business money: opening an account and the **right to an account** when refused, credit and **credit withdrawal**, **personal guarantees given by a director**, cash flow, credit mediation, mandatory insurance. |
| **Patrimoine** | `/patrimoine` | Your personal money: ⚠️ **spotting a financial scam and checking that a firm is authorised**, savings wrappers, fees, risk and horizon, regulated savings and deposit guarantees, retirement, budgeting and **over-indebtedness**. |
| **Juriste** | `/juriste` | Companies, contracts and T&Cs, cross-border work, intellectual property, regulated activities, consumer law, GDPR, civil procedure. |
| **Travail** | `/travail` | Employment: collective agreement, contract, pay and working time, dismissal and severance, labour court, harassment and discrimination. |
| **Logement** | `/logement` | Renting: lease, deposit, notice, charges and repairs, arrears and eviction, flat-sharing, co-ownership. |
| **Famille** | `/famille` | Couple and matrimonial regimes, separation, children and maintenance, inheritance, gifts, protection of vulnerable adults, domestic violence. |
| **Immigration** | `/immigration` | Residence permits, renewals, change of status, right to work, family, refusals and appeals, **French citizenship**. |

**A role is not a topic.** It is an entry method, a posture and its own stopping rules. `/travail`
starts by asking which collective agreement applies, `/immigration` starts by looking for a deadline
already running, `/logement` starts by reading the law before the lease. The criterion that decides
when a subject deserves its own role is in [`docs/taxonomie.md`](docs/taxonomie.md).

## ★ The one rule: no figure is ever written from memory

French tax and social rules change every year, sometimes mid-year. A skill that recites last year's
rate with confidence is **more dangerous than no skill at all**: it produces a confident error that
nobody has a reason to double-check, and decisions get built on it.

So, here:

1. **`data/parametres.json` is authoritative.** Every value carries its `source` (an official URL)
   and its `date_verifiee`. If a prose file disagrees with it, **the JSON wins**.
2. **A prose file may quote a value only if that value also lives in its role's JSON**, sourced and
   dated. A number that exists only in prose is a number nobody will be able to date later.
3. **The skill refuses to assert a stale value.** Past six months it says so and points you to the
   source instead of guessing.
4. **And the promise is verifiable, not declarative:**

```bash
python scripts/verifier-parametres.py
```

The script fails if a value claims to be verified without a source or a date, if a source falls
outside the list of official domains, if a number quoted in a `.md` exists in no JSON, if a file is
routed by no `SKILL.md`, if an image is missing, or if a role is not installable. **It runs in CI on
every push.**

> ⚠️ **This repository has been wrong before, and will always say so.** An adversarial review found
> three false statements published as verified: a supposedly retroactive VAT threshold, an outdated
> relief rate, and a suspensive effect of appeal stated backwards — the last one being the dangerous
> one, since it could have discouraged someone from filing the appeal that protected them. All three
> are corrected, the JSON notes keep the trace, and the script above was born from that episode.
> **A claim of accuracy that hides its own errors is not a claim.**

## Install

```bash
/plugin marketplace add Sjrazaviebra/le-cabinet
```

```bash
/plugin install juridique@le-cabinet
```

```bash
/plugin install comptabilite@le-cabinet
```

⚠️ **Domains install, not individual roles.** `juridique` brings five roles, `comptabilite` brings
four. Installed as plugins, skills are **namespaced**: `/juridique:travail`, not `/travail`.

Using another agent than Claude? The content is portable — see [`AGENTS.md`](AGENTS.md).

## ⚖️ What these roles are not

They do **not** replace a lawyer admitted to the bar, a chartered accountant, or a registered
investment adviser. They are **decision-support tools**: they structure a question, ask the right
ones, and tell you **where to verify**. For anything binding — signing a contract, filing a return,
going to court — consult a professional carrying professional indemnity insurance.

⛔ And two roles carry a sharper line: `financement` and `patrimoine` **inform**, they do not advise.
They issue no personalised recommendation on a financial instrument — that is regulated investment
advice — and they recommend no bank, product or provider. The analysis of where exactly that line
falls is in [`docs/taxonomie-comptabilite.md`](docs/taxonomie-comptabilite.md).

## Licence

MIT — see [`LICENSE`](LICENSE). Contributions welcome: read
[`CONTRIBUTING.md`](CONTRIBUTING.md) first, and note that **the gate applies to contributions too**.
