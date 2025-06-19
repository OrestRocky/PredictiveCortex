package agent

import "fmt"

type Agent struct {
	Name    string
	Beliefs []string
	Goals   []string
}

func (a Agent) ReactTo(situation string) string {
	for _, belief := range a.Beliefs {
		if belief == situation {
			return fmt.Sprintf("%s takes action due to belief: %s", a.Name, belief)
		}
	}
	return fmt.Sprintf("%s observes situation: %s with no immediate action", a.Name, situation)
}
