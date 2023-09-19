package config

import (
	"os"
)

// Configuration struct to hold your application's settings
type AppConfig struct {
	Port     string
	Database string
}

// NewAppConfig creates a new AppConfig instance with default values
func NewAppConfig() AppConfig {
	return AppConfig{
		Port:     getEnv("PORT", "3000"),     // Default to 8080 if PORT environment variable is not set
		Database: getEnv("DATABASE_URL", ""), // Default to empty string if DATABASE_URL is not set
	}
}

// getEnv is a helper function to read environment variables
func getEnv(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok {
		return value
	}
	return fallback
}
