from collections import namedtuple

Servant = namedtuple('Servant', ['name', 'ascension', 'skills', 'priority'])

servants = [
    Servant('Miyamoto Musashi', 5, [10,10,10], 1),
    Servant('Arthur Pendragon (Prototype)', 5, [6,6,6], 1),
    Servant('Nero Claudius (Bride)', 5, [10,10,6], 1),
    Servant('Okita Souji', 5, [6,6,6], 1),
    Servant('Nikola Tesla', 5, [10,10,10], 1),
    Servant('Karna', 5, [6,8,10], 1),
    Servant('Altria Pendragon (Rider Alter)', 5, [10,6,6], 1),
    Servant('Merlin', 5, [10,10,10], 1),
    Servant('Xuanzang Sanzang', 5, [10,6,10], 1),
    Servant('First Hassan', 5, [6,10,10], 1),
    Servant('Sessyoin Kiara', 5, [6,6,6], 1),
    Servant('Katsushika Hokusai', 5, [10,10,10], 1),
    Servant('Abigail Williams', 5, [10,6,6], 1),
    Servant('Elisabeth Bathory (Brave)', 5, [1,1,1], 2),
    Servant("Chevalier d'Eon", 5, [4,3,5], 2),
    Servant('Attila the San(ta)', 5, [6,6,6], 2),
    Servant('Archer of Inferno', 5, [6,6,6], 2),
    Servant('Oda Nobunaga', 5, [6,6,6], 2),
    Servant('EMIYA', 5, [6,6,6], 2),
    Servant("Jeanne d'Arc (Alter Santa Lily)", 5, [6,6,6], 2),
    Servant('Altria Pendragon (Lancer Alter)', 5, [6,6,6], 1),
    Servant('Elisabeth Bathory', 5, [6,6,6], 2),
    Servant('Ishtar (Rider)', 5, [6,6,6], 2),
    Servant('Sakata Kintoki (Rider)', 5, [9,7,6], 2),
    Servant('Saint Martha', 5, [6,6,6], 2),
    Servant('Caster of Midrash', 5, [6,6,6], 2),
    Servant('Gilgamesh (Caster)', 5, [6,6,6], 2),
    Servant('Nitocris', 5, [6,8,6], 1),
    Servant('Assassin of Paraiso', 5, [6,6,6], 3),
    Servant('Scathach (Assassin)', 5, [6,6,6], 2),
    Servant('Ryougi Shiki (Assassin)', 4, [6,6,6], 1),
    Servant('Chacha', 5, [1,1,1], 3),
    Servant('Heracles', 5, [8,7,6], 2),
    Servant('Saint Martha (Ruler)', 5, [6,6,6], 2),
    Servant('Gorgon', 5, [9,6,6], 2),
    Servant('Mecha Eli-chan', 5, [6,6,6], 2),
    Servant('BB', 5, [10,6,6], 1),
    Servant('Mash Kyrielight', 5, [9,8,6], 2),
    Servant('Frankenstein', 5, [6,6,6], 1),
    Servant('Passionlip', 5, [6,6,6], 2),
    Servant('Bedivere', 5, [6,1,6], 3),
    Servant('Fergus mac Roich', 5, [4,4,2], 3),
    Servant('Gaius Julius Caesar', 5, [2,6,1], 3),
    Servant('Asagami Fujino', 2, [6,2,4], 1),
    Servant('David', 5, [4,2,1], 2),
    Servant('Euryale', 5, [4,1,6], 2),
    Servant('Robin Hood', 5, [1,1,1], 3),
    Servant('Jaguar Warrior', 5, [1,1,1], 3),
    Servant('Cu Chulainn', 5, [1,1,2], 3),
    Servant('Ushiwakamaru', 5, [4,8,1], 3),
    Servant('Medusa', 5, [2,1,1], 3),
    Servant('Nursery Rhyme', 5, [1,1,1], 3),
    Servant('Medea', 5, [1,1,1], 3),
    Servant('Hassan of the Serenity', 5, [1,1,1], 3),
    Servant('Fuuma Kotarou', 5, [1,1,1], 3),
    Servant('Hassan of the Hundred Personas', 5, [1,1,1], 3),
    Servant('Lu Bu Fengxian', 5, [1,1,1], 3),
    Servant('Boudica', 5, [1,1,1], 3),
    Servant('Sieg', 4, [1,1,1], 2),
    Servant('Leonidas', 5, [1,1,1], 3),
    Servant('Georgios', 5, [1,1,1], 2),
    Servant('Hans Christian Andersen', 5, [1,6,1], 3),
    Servant('Hassan of the Cursed Arm', 5, [2,2,2], 3),
    Servant('Altria Pendragon (Lily)', 4, [1,1,1], 3),
    Servant('Arash', 5, [1,1,5], 3),
    Servant('Mata Hari', 5, [1,1,1], 3),
    Servant('Paul Bunyan', 5, [1,1,1], 2),
    Servant('Spartacus', 5, [1,4,1], 3),
    Servant('Sakamoto Ryouma', 3, [1,1,1,], 2),
    Servant('EMIYA (Assassin)', 2, [1,1,1], 3),
    Servant('Jing Ke', 3, [2,1,1], 3),
    Servant('Asterios', 3, [1,1,1], 3),
    Servant('Diarmuid ua Duibhne', 2, [1,1,1], 3),
    Servant('Kid Gilgamesh', 2, [6,1,1], 3),
    Servant('William Shakespeare', 3, [1,1,1], 3),
    Servant('Cu Chulainn (Prototype)', 2, [1,1,1], 3),
    Servant('Charles-Henri Sanson', 2, [1,2,1], 3),
    Servant('Kiyohime', 1, [1,1,1], 3),
    Servant('Fionn mac Cumhaill', 1, [1,1,1], 2),
    Servant('Gilles de Rais', 1, [1,1,1], 3),
    Servant('Sasaki Kojirou', 2, [2,1,1], 3),
    Servant('Musashibou Benkei', 1, [1,1,1], 3),
    Servant('Phantom of the Opera', 1, [1,1,1], 3),
    Servant('Ibaraki-Douji', 1, [1,1,1], 2),
    Servant('Tawara Touta', 1, [1,1,1], 3),
    Servant('Billy the Kid', 1, [1,1,1], 3),
    Servant('Houzouin Inshun', 1, [1,1,1], 3),
    Servant('Hektor', 1, [1,1,1], 3),
    Servant('Romulus', 1, [1,1,1], 3),
    Servant('Alexander', 1, [1,1,1], 3),
    Servant('Edward Teach', 1, [1,1,1], 3),
    Servant('Avicebron', 1, [1,1,1], 3),
    Servant('Geronimo', 1, [1,1,1], 3),
    Servant('Charles Babbage', 1, [1,1,1], 3),
    Servant('Paracelsus von Hohenheim', 1, [1,1,1], 2),
    Servant('Cu Chulainn (Caster)', 1, [1,1,1], 3),
    Servant('Mephistopheles', 1, [1,1,1], 3),
    Servant('Gilles de Rais (Caster)', 1, [1,1,1], 3),
    Servant('Wolfgang Amadeus Mozart', 1, [1,1,1], 3),
    Servant('Okada Izo', 1, [1,1,1], 2),
    Servant('Henry Jekyll & Hyde', 1, [1,1,1], 3),
    Servant('Darius III', 1, [1,1,1], 3),
    Servant('Eric Bloodaxe', 1, [1,1,1], 3),
    Servant('Caligula', 1, [1,1,1], 3),
    Servant('Antonio Salieri', 1, [1,1,1], 3)
]

Material = namedtuple('Material', ['name', 'amount'])

materials = [
    Material('Gem of Saber', 14),
    Material('Gem of Archer', 8),
    Material('Gem of Lancer', 113),
    Material('Gem of Rider', 89),
    Material('Gem of Caster', 12),
    Material('Gem of Assassin', 118),
    Material('Gem of Berserker', 160),
    Material('Magic Gem of Saber', 10),
    Material('Magic Gem of Archer', 1),
    Material('Magic Gem of Lancer', 113),
    Material('Magic Gem of Rider', 63),
    Material('Magic Gem of Caster', 17),
    Material('Magic Gem of Assassin', 124),
    Material('Magic Gem of Berserker', 124),
    Material('Secret Gem of Saber', 3),
    Material('Secret Gem of Archer', 84),
    Material('Secret Gem of Lancer', 79),
    Material('Secret Gem of Rider', 99),
    Material('Secret Gem of Caster', 88),
    Material('Secret Gem of Assassin', 82),
    Material('Secret Gem of Berserker', 102),
    Material('Proof of Hero', 14),
    Material('Evil Bone', 20),
    Material('Dragon Fang', 255),
    Material("Void's Dust", 102),
    Material("Fool's Chain", 93),
    Material('Deadly Poisonous Needle', 128),
    Material('Mystic Spinal Fluid', 219),
    Material('Stake of Wailing Night', 13),
    Material('Mystic Gunpowder', 50),
    Material('Seed of Yggdrasil', 128),
    Material('Ghost Lantern', 97),
    Material('Octuplet Crystals', 75),
    Material('Serpent Jewel', 164),
    Material('Phoenix Feather', 92),
    Material('Eternal Gear', 96),
    Material('Forbidden Page', 76),
    Material('Homunculus Baby', 146),
    Material('Meteor Horseshoe', 122),
    Material('Great Knight Medal', 164),
    Material('Shell of Reminiscence', 32),
    Material('Refined Magatama', 46),
    Material('Eternal Ice', 31),
    Material('Claw of Chaos', 170),
    Material('Heart of the Foreign God', 163),
    Material("Dragon's Reverse Scale", 108),
    Material('Spirit Root', 94),
    Material("Warhorse's Young Horn", 105),
    Material('Tearstone of Blood', 149),
    Material('Black Beast Grease', 44),
    Material('Lamp of Evil-Sealing', 116),
    Material('Scarab of Wisdom', 102),
    Material('Primordial Lanugo', 148),
    Material('Cursed Beast Gallstone', 55),
    Material('Mysterious Divine Wine', 102),
    Material('Crystallized Lore', 40),
    Material('Saber Piece', 41),
    Material('Archer Piece', 74),
    Material('Lancer Piece', 101),
    Material('Rider Piece', 74),
    Material('Caster Piece', 80),
    Material('Assassin Piece', 98),
    Material('Berserker Piece', 110),
    Material('Saber Monument', 76),
    Material('Archer Monument', 82),
    Material('Lancer Monument', 144),
    Material('Rider Monument', 116),
    Material('Caster Monument', 97),
    Material('Assassin Monument', 94),
    Material('Berserker Monument', 143),
    Material('Piece of Ranjatai', 4),
    Material('Leaf of Remembrance', 1),
    Material('Kaientai Banner', 2)
]
