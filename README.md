# Antidote  
<img src="src/bsrc/docs/antidote.png" alt="Antidote Logo" width="300">

**Antidote** is an experimental encryption algorithm with a minimal UI for sending messages — locally, securely, and without oversight.


## Why should we care?

Because we don’t.  
Sell drugs, talk about aliens, or plan your next Fortnite match, whatever.  
Antidote makes sure no one else sees that message.  

This isn’t another messaging app.  
This is a **protest** against forced identification and chat surveillance.  
No sign-ins. No phone numbers. No cloud. Just math and silicone.


## What it does (for now)

- Generates **public/private keypairs** using a custom elliptic curve system.  
- Encrypts and signs messages locally.  
- Decrypts messages using receiver keys.  
- Keeps everything **offline** and **local**, meaning no external servers.  

At this point, it’s more like **PGP with attitude** than a finished messenger.


## In progress

- Implementing full message authentication and signature verification.  
- Integrating a local message UI.  
- Experimenting with **Tor routing** for peer-to-peer communication.  
- Planning compression + QR encoding for message transfer.

## Config Explained

```

# messages:
# saves the senders private key, and receivers public key along with the encrypted message
# (meaning that you can only save message you sent)
# future server implementations will have message sharing protocols

storing_messages = True # can be set to "Flase"
number_of_saved_messages = 10 # if storing_messages = False, then this number dosent get used

# keypairs:
# saves YOUR last 10 keypairs
# seed, public key and private key

storing_keypairs = True # can be se to "False"
number_of_saved_keypairs = 10 # if storing_keypairs = False, then this number dosent get used

# contacts:
# saves the public key of your last n messages
# (meaning that if the person dosent have access to that keypair, you will have to find his latest keypair somehow otherwise)

# IMPORTAINT:
# if you stop talking to a person, tell them to keep the keypair that you will send the message to (and vice versa)
# so that when you comeback, that person still has access to the keypair and can decrypt your message, or do a handshake to get both clients a new fingerprint

storing_contacts = True # can be set to "False"
number_of_saved_contacts = 10 # if storing_contacts = False, then this number dosent get used.

```

## Structure (rough)

```
antidote/
├── src/
│ ├── core/ # encryption logic
│ ├── network/ # Tor network placeholder
│ ├── ui/ # user interface
│ ├── bsrc/docs/ # images + markdown stuff
│ └── tests/ # early testing scripts
├── README.md
├── LICENCE
├── .gitignore
└── requierments.txt

```

## Status

Work in progress, currently prototyping the algorithm’s **core logic** before UI + network integration.  
If you’re reading this, you’re early. Like, pre-alpha early.


## Future vision

A local-first, Tor-connected messaging app that nobody controls, and nobody can trace.  
Not another social platform. just **encrypted freedom**.

## Disclaimer

This project is **for educational and privacy research** purposes.  
Not intended for illegal use. You break it, you buy it.


### Made with a dream and caffeine, please open issues with my code
