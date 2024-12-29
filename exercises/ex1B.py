import threading
import time
import random


class TrainStation:
    def __init__(self, n_tracks):
        """Initialize the train station with n_tracks and locks."""
        self.n_tracks = n_tracks
        self.tracks = [False] * n_tracks  # Tracks: True if occupied, False if free
        self.lock = threading.Lock()  # Lock to ensure thread-safe access to tracks

    def occupy_track(self, train_name):
        """Occupy the first available track."""
        with self.lock:  # Ensure thread-safe access to the tracks
            for i in range(self.n_tracks):
                if not self.tracks[i]:  # Find the first free track
                    self.tracks[i] = True
                    print(f"{train_name} occupied track {i + 1}")
                    return i
        return -1  # No track available (shouldn't happen due to semaphore control)

    def release_track(self, track_number, train_name):
        """Release the given track."""
        with self.lock:
            self.tracks[track_number] = False  # Free the track
            print(f"{train_name} released track {track_number + 1}")


class Train(threading.Thread):
    def __init__(self, station, train_name, semaphore):
        """Initialize the train thread."""
        super().__init__()
        self.station = station
        self.train_name = train_name
        self.semaphore = semaphore

    def run(self):
        """Simulate train behavior."""
        try:
            # Simulate random delay before trying to occupy a track
            time.sleep(random.uniform(0.1, 1.0))

            # Acquire semaphore to proceed with track occupation
            self.semaphore.acquire()

            # Occupy a track
            track_number = self.station.occupy_track(self.train_name)

            # Simulate random time spent on the track
            time.sleep(random.uniform(0.5, 2.0))

            # Release the track
            self.station.release_track(track_number, self.train_name)

        finally:
            # Release semaphore so another train can proceed
            self.semaphore.release()


if __name__ == "__main__":
    # Initialize station and parameters
    n_tracks = 5  # Number of tracks
    n_trains = 20  # Number of trains

    station = TrainStation(n_tracks)
    semaphore = threading.Semaphore(n_tracks)  # Semaphore to control track access

    # Create and start train threads
    trains = []
    for i in range(n_trains):
        train_name = f"Train-{i + 1}"
        train = Train(station, train_name, semaphore)
        trains.append(train)
        train.start()

    # Wait for all trains to complete
    for train in trains:
        train.join()

    print("All trains have completed their operations.")
