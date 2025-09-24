import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import React from 'react';
import { Pressable, StyleSheet } from 'react-native';

export default function HomeScreen() {
  return (
    <ThemedView style={styles.container}>
      <ThemedText type="title" style={styles.title}>
        Welcome to My Game!
      </ThemedText>

      <ThemedText style={styles.subtitle}>
        Get ready for an exciting adventure.  
        Tap the button below to start playing.
      </ThemedText>

      {/* Link navigates to the /Chaturanga page */}
      <Link href="/Chaturanga" asChild>
        <Pressable style={styles.playButton}>
          <ThemedText type="subtitle" style={styles.buttonText}>
            Play Game
          </ThemedText>
        </Pressable>
      </Link>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#4F46E5', // Indigo background
  },
  title: {
    marginBottom: 16,
    color: '#FFFFFF',
  },
  subtitle: {
    textAlign: 'center',
    color: '#E0E7FF',
    marginBottom: 40,
  },
  playButton: {
    backgroundColor: '#FFFFFF',
    paddingVertical: 14,
    paddingHorizontal: 40,
    borderRadius: 12,
    elevation: 4,
  },
  buttonText: {
    color: '#4F46E5',
    fontWeight: 'bold',
  },
});
