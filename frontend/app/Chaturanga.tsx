import React, { useRef } from 'react';
import {
  Dimensions,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View
} from 'react-native';

// --- CONSTANTS (unchanged) ---
const BOARD_SIZE = 8;
const PLAYERS = [
  { id: 'red', name: 'Red', color: '#8a1515', alliance: 1 },
  { id: 'yellow', name: 'Yellow', color: '#e8af28', alliance: 2 },
  { id: 'black', name: 'Black', color: '#0e0d0d', alliance: 1 },
  { id: 'white', name: 'White', color: '#ebeef0', alliance: 2 },
];
const PIECE_TYPES = {
  PAWN: { name: 'Pawn', symbol: '♙' },
  BOAT: { name: 'Boat', symbol: '♝' },
  HORSE: { name: 'Horse', symbol: '♞' },
  ELEPHANT: { name: 'Elephant', symbol: '♜' },
  KING: { name: 'King', symbol: '♚' },
};
const PIECE_VALUES = { Pawn: 1, Boat: 5, Horse: 5, Elephant: 5, King: 5 };
const DICE_MAP = {
  2: PIECE_TYPES.BOAT.name,
  3: PIECE_TYPES.HORSE.name,
  4: PIECE_TYPES.ELEPHANT.name,
  5: PIECE_TYPES.KING.name,
};
const INITIAL_BOARD_STATE = [/* ...same as before... */];

// --- MAIN COMPONENT ---
export default function Chaturanga() {
  const boardRef = useRef<ScrollView>(null);

  const scrollToBoard = () => {
    boardRef.current?.scrollTo({ y: Dimensions.get('window').height * 0.9, animated: true });
  };

  return (
    <ScrollView
      ref={boardRef}
      style={styles.page}
      contentContainerStyle={{ paddingBottom: 40 }}
    >
      {/* ---- Intro Section ---- */}
      <View style={styles.intro}>
        <Text style={styles.heading}>Chaturanga</Text>
        <Text style={styles.subheading}>
          The Ancient Indian Strategy Game, Precursor to Modern Chess
        </Text>
        <Text style={styles.paragraph}>
          Chaturanga, meaning "four limbs," is a two-player strategy game that
          originated in ancient India. It's a game of wit and foresight,
          reflecting the four divisions of a traditional army: infantry,
          cavalry, elephantry, and chariotry. Master the battlefield and
          checkmate your opponent's Raja.
        </Text>
        <TouchableOpacity style={styles.playBtn} onPress={scrollToBoard}>
          <Text style={styles.playBtnText}>Play Now</Text>
        </TouchableOpacity>
      </View>

      {/* ---- Pieces Description ---- */}
      <View style={styles.piecesSection}>
        <Text style={styles.sectionTitle}>The Pieces</Text>
        {[
          { title: 'Raja (King)', desc: 'Moves one square in any direction, just like the modern king. Protect your Raja and checkmate the opponent.' },
          { title: 'Mantri (Minister)', desc: 'Moves one square diagonally. A key advisor to the Raja.' },
          { title: 'Gaja (Elephant)', desc: 'Moves two squares diagonally, jumping over pieces.' },
          { title: 'Ashva (Horse)', desc: 'Moves in an L-shape and can jump over pieces.' },
          { title: 'Ratha (Chariot)', desc: 'Moves any number of squares horizontally or vertically.' },
          { title: 'Padati (Foot Soldier)', desc: 'Moves one square forward and captures diagonally.' },
        ].map((p, i) => (
          <View key={i} style={styles.card}>
            <Text style={styles.cardTitle}>{p.title}</Text>
            <Text style={styles.cardText}>{p.desc}</Text>
          </View>
        ))}
      </View>
      {/* ---- Game Board Placeholder ---- */}
      <View style={styles.gameContainer}>
        <Text style={styles.gameTitle}>
          Chaturanga - The Four-Player Ancient Chess
        </Text>
        {/* Your actual board UI / logic goes here */}
      </View>
    </ScrollView>
  );
}

// --- STYLES ---
const styles = StyleSheet.create({
  page: { flex: 1, backgroundColor: '#d2b48c' },

  intro: {
    padding: 20,
    alignItems: 'center',
    backgroundColor: '#f5deb3',
  },
  heading: {
    fontSize: 36,
    fontWeight: '800',
    backgroundColor: 'transparent',
    color: '#b8860b',
    textAlign: 'center',
  },
  subheading: {
    fontSize: 18,
    color: '#555',
    textAlign: 'center',
    marginVertical: 10,
  },
  paragraph: {
    fontSize: 16,
    color: '#444',
    textAlign: 'center',
    marginBottom: 20,
  },
  playBtn: {
    backgroundColor: '#333',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 25,
  },
  playBtnText: { color: '#fff', fontSize: 18, fontWeight: 'bold' },

  piecesSection: { padding: 20 },
  sectionTitle: {
    fontSize: 28,
    fontWeight: '700',
    textAlign: 'center',
    color: '#b8860b',
    marginBottom: 15,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 16,
    marginVertical: 8,
    shadowColor: '#000',
    shadowOpacity: 0.15,
    shadowOffset: { width: 0, height: 3 },
    shadowRadius: 5,
    elevation: 3,
  },
  cardTitle: { fontSize: 20, fontWeight: '700', color: '#e1a100', marginBottom: 4 },
  cardText: { fontSize: 16, color: '#444' },

  gameContainer: {
    padding: 20,
    backgroundColor: '#1B263B',
    alignItems: 'center',
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    marginTop: 20,
  },
  gameTitle: { fontSize: 22, fontWeight: 'bold', color: '#ecf0f1', marginBottom: 10 },
});

